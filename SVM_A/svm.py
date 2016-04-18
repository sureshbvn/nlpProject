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
t = " -t 1 "
c = " -c 1 "
m = " -m 1024 "
w0 = " -w0 0.0384 "
w1 = " -w1 1.136 "
w2 = " -w2 0.37 "
w3 = " -w3 0.33 "
w4 = " -w4 0.20 "
w5 = " -w5 0.0164 "
d = " -d 4 "

predictFile = properties.test_features_file_path

def SVMTrain(feature):
    print 'SVM training started...\n'
    cmd = "\""+svm+config[0]+"\""+ t + c + m + w0 + w1 + w2 + w3 + w4 + w5 +d +feature+" "+model
    print cmd
    os.system(cmd)
    print 'SVM training finished\n'

def SVMPreditct():
    cmd = "\""+svm+config[1]+"\""+" "+predictFile+" "+model+" "+output
    print cmd
    os.system(cmd)

if __name__=="__main__":

    #SVMTrain(properties.feature_file_path)
    SVMPreditct()