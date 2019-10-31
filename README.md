***-----***
## Pre-requisites
h5py==2.9.0
Keras==2.2.4
numpy==1.16.2
opencv_python==4.1.0.25
setuptools==39.1.0
PyQt5==5.11.3

## h5 model to pb model
python ht_pb.py
python test_pb.py

## run
python DenoisingMainWin.py

## test data path
需要恢复的扫描试卷示例图像在./blur_data下，选择模型文件在./checkpoints下，恢复后可以将结果文件进行保存。
