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
c = " -c 10 "
w = " -w0 3.81 -w1 119.19 -w2 37.19 -w3 30 -w4 19.59 -w5 1.61 "
predictFile = properties.test_features_file_path

def SVMTrain(feature):
    cmd = "\""+svm+config[0]+"\""+t+c+w+feature+" "+model
    os.system(cmd)

def SVMPreditct():
    cmd = "\""+svm+config[1]+"\""+" "+predictFile+" "+model+" "+output
    os.system(cmd)

if __name__=="__main__":
   featureFile = properties.feature_file_path
   SVMTrain(featureFile)

   #SVMPreditct()
   print("done")