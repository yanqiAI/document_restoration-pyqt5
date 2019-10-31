# coding:utf-8
import os
import numpy as np
import cv2
import time
import h5py
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_win import *
import sys
import tensorflow as tf
from tensorflow.python.platform import gfile
from pathlib import Path

class load_bp():
    def __init__(self):
        # load pb file
        self.pb_path = 'pb_model/model_restoration.pb'
        self.sess = tf.Session()
        init = tf.global_variables_initializer()
        self.sess.run(init)
        with tf.gfile.FastGFile(self.pb_path, "rb") as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            self.sess.graph.as_default()
            tf.import_graph_def(graph_def, name="")
        self.inputs = self.sess.graph.get_tensor_by_name('input_1:0')
        self.outputs = self.sess.graph.get_tensor_by_name('output_1:0')

    def denoised(self, img):
        denoised_img = self.sess.run(self.outputs, feed_dict={self.inputs: np.expand_dims(img[:, :, np.newaxis], 0)}).squeeze()
        return denoised_img


class MyImageDenoisingWindow(QMainWindow, Ui_Window):
    def __init__(self, parent = None):
        super(MyImageDenoisingWindow, self).__init__(parent)
        self.setupUi_denoising(self)
        self.pb = load_bp()

    def clip_one_test(self, img, img_size=256):
        img_h, img_w = img.shape[:2]

        # clip m * n
        m = img_h // img_size
        n = img_w // img_size
        gh = m * img_size
        gw = n * img_size
        img_resize = cv2.resize(img, (gw, gh), interpolation=cv2.INTER_LINEAR)

        # processing
        gx, gy = np.meshgrid(np.linspace(0, gw, n + 1), np.linspace(0, gh, m + 1))
        gx = gx.astype(np.int)
        gy = gy.astype(np.int)

        divide_image = np.zeros([m, n, img_size, img_size], np.uint8)

        clip_images = []
        for i in range(m):
            for j in range(n):
                divide_image[i, j, ...] = img_resize[gy[i][j]:gy[i+1][j+1], gx[i][j]:gx[i+1][j+1]]
                clip_images.append(divide_image[i, j, ...])

        return clip_images, m, n

    def merge_cliped_data(self, cliped_images, m, n, img_size = 256):
        '''
        :param cliped_images: cliped list
        :param m: the number of rows
        :param n: the number of cols
        :param img_size: cliped image size (default=256*256)
        :return: dst: merged image
        '''
        gh = m * img_size
        gw = n * img_size

        gx, gy = np.meshgrid(np.linspace(0, gw, n + 1), np.linspace(0, gh, m + 1))
        gx = gx.astype(np.int)
        gy = gy.astype(np.int)
        dst = np.zeros((gh, gw), np.float32)

        count = 0
        for i in range(m):
            for j in range(n):
                dst[gy[i][j]:gy[i+1][j+1], gx[i][j]:gx[i+1][j+1]] = cliped_images[count]
                count += 1

        return dst

    def bnt1_click(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "选择要恢复的图像", './dataset', '*.png *.jpg *.bmp')
        if self.filename is '':
            return
        self.lineEdit1.setText(self.filename)
        # jpg = QtGui.QPixmap(self.filename, '1').scaled(self.labelpix1.size(), QtCore.Qt.KeepAspectRatio)
        # self.labelpix1.setPixmap(jpg)
        jpg = QtGui.QPixmap(self.filename).scaled(self.labelpix1.width(), self.labelpix1.height())
        self.labelpix1.setPixmap(jpg)

    def bnt3_click(self):
        image_dir = self.filename

        # load image
        # opencv imread, Chinese path is not support!!!
        # image = cv2.imread(image_dir, 0)
        image = cv2.imdecode(np.fromfile(image_dir, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
        h, w = image.shape

        start_time = time.time()

        # if image size is too large
        if h > 256 or w > 256:
            # clip image to 256*256 blocks
            cliped_image, m, n = self.clip_one_test(image)

            denoised = []
            for img in cliped_image:
                pred = self.pb.denoised(img)
                denoised.append(pred)

            # merge denoised results
            dst = self.merge_cliped_data(denoised, m, n, img_size=256)
            self.denoised = cv2.resize(dst, (w, h), interpolation=cv2.INTER_LINEAR)

        else:
            image = image[:(h // 16) * 16, :(w // 16) * 16]  # for stride (maximum 16)
            # h, w = image.shape
            self.denoised = self.pb.denoised(image)

        end_time = time.time()
        cost_time = end_time - start_time

        # show denoising result
        self.denoised_image = np.clip(self.denoised, 0, 255).astype(dtype=np.uint8)
        bytesPerLine = 1 * w
        denoised_image_ = QtGui.QImage(self.denoised_image.data, w, h, bytesPerLine, QtGui.QImage.Format_Grayscale8)
        denoised_image_ = QtGui.QPixmap.fromImage(denoised_image_).scaled(self.labelpix2.width(), self.labelpix2.height())
        self.labelpix2.setPixmap(denoised_image_)
        self.labeltime.setText('恢复这张图片用时: {}s'.format(str(round(cost_time, 4))))

    def bnt4_click(self):
        fileName, tmp = QtWidgets.QFileDialog.getSaveFileName(self, "保存恢复图像", './results', '*.png *.jpg *.bmp')
        if fileName is '':
            return
        if self.denoised_image.size == 1:
            return
        cv2.imwrite(fileName, self.denoised_image)
        self.labelsave.setText('图片保存成功！')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyImageDenoisingWindow()
    myWin.show()
    sys.exit(app.exec_())