from __future__ import division
import re
import numpy as np
import sklearn.metrics as grading_metrics
import utility as util
import string

fw=open("tempout.txt","w+")

def transform(line):
    if len(line)==0:
        return

    if line[-1] is not '.' and line[-1] is not ',':
        line = line + '.'
    line += '$'

    newline = re.sub("\, ",",",line)
    newline = re.sub("\. ",".",newline)
    newline = re.sub(" "," epsilon ",newline)
    newline = re.sub("\. ",' .PERIOD ',newline)
    newline = re.sub("\.\$"," .PERIOD ",newline)
    newline = re.sub("\,",' ,COMMA ',newline)
    fw.write(newline+"\n")
    return newline+'\n'

def determine_class(word,punc):

    class_label = 100
    if util.isCaptilized(word) and punc=="epsilon":
        class_label = 0
    elif util.isCaptilized(word) and punc=='.PERIOD':
        class_label = 1
    elif util.isCaptilized(word) and punc==',COMMA':
        class_label = 2
    elif punc == '.PERIOD':
        class_label = 3
    elif punc == ',COMMA':
        class_label = 4
    else:
        class_label = 5
    return class_label


if __name__=="__main__":
    string = open('uncleaned_test_data.txt').readlines()
    new_string = []
    for line in string:

        str1=line[:-1]
        if len(str1)>0:
            newline = transform(str1)
            new_string.append(newline)


    string = open('output.txt','r')
    final_actual_list= []
    final_predicted_list = []

    for line_actual in new_string:
        line_predicted = string.readline()
        if len(line_predicted)==1:
            line_predicted = string.readline()


        line_predicted = line_predicted[:-1]
        actual_list = line_actual.split(" ")
        actual_list = actual_list[:-1]

        if len(line_predicted)<=0:
            continue

        predicted_list = line_predicted.split()
        if len(actual_list)!=len(predicted_list):
            continue



        for i in xrange(0,len(actual_list),2):



            word = actual_list[i]

            actual_punc = actual_list[i+1]



            predicted_punc = predicted_list[i+1]






            actual_class = determine_class(word,actual_punc)
            predicted_class = determine_class(word,predicted_punc)
            final_actual_list.append(actual_class)
            final_predicted_list.append(predicted_class)



    new_accuracy = grading_metrics.accuracy_score(final_actual_list,final_predicted_list)
    print "accuracy = "
    print new_accuracy

    #f1_score = grading_metrics.f1_score(actual,predicted,average=None)
    f_score = grading_metrics.precision_recall_fscore_support(final_actual_list,final_predicted_list,average=None)
    print("\nprecision :" )
    class_index = 0
    for class_precision in f_score[0]:
        print("for class ")
        print class_index+1
        print class_precision
        class_index+=1

    print("\nrecall :" )
    class_index = 0
    for class_recall in f_score[1]:
        print("for class "+str(class_index+1) + " "+ str(class_recall))
        class_index+=1

    print("\nf_measure :" )
    class_index = 0
    for class_f in f_score[2]:
        print("for class "+str(class_index+1) + " "+ str(class_f))
        class_index+=1

    f1_score = grading_metrics.f1_score(final_actual_list,final_predicted_list,average=None)
    print("\nf1_measure :" )
    class_index = 0
    for class_f1 in f1_score:
        print("for class "+str(class_index+1) + " "+ str(class_f1))
        class_index+=1