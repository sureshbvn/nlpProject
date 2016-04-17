import os
import sys
import numpy as np
import properties

svm = properties.svm_path
model = properties.svm_model_path
output = properties.svm_output_path
config = []
config.append("bsvm-train.exe")
config.append("bsvm-predict.exe")
t = " -t 0 "
c = " -c 1 "
m = " -m 2048 "
w0 = " -w0 2 "
w1 = " -w1 15 "
w2 = " -w2 15 "
w3 = " -w3 10 "
w4 = " -w4 5 "
w5 = " -w5 1 "

predictFile = properties.test_features_file_path

def SVMTrain(feature):
    print 'SVM training started...\n'
    cmd = "\""+svm+config[0]+"\""+ t + c + m + w0 + w1 + w2 + w3 + w4 + w5 + feature+" "+model
    print cmd
    os.system(cmd)
    print 'SVM training finished\n'

def SVMPreditct():
    cmd = "\""+svm+config[1]+"\""+" "+predictFile+" "+model+" "+output
    os.system(cmd)

if __name__=="__main__":

    SVMTrain(properties.feature_file_path)
    #SVMPreditct()

