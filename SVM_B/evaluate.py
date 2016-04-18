from __future__ import division
import re
import numpy as np
import sklearn.metrics as grading_metrics


if __name__=="__main__":
    string = open('testOutput.txt').readlines()
    new_string = ""
    for line in string:
        class_label = line[0]
        new_string = new_string + class_label + "\n"
    actual = re.findall('\d+', new_string)
    #print(actual)

    string = open('classified.txt').read()
    predicted = re.findall('\d+', string)
    #print(predicted)


    correct = 0
    for i in range(len(predicted)):
        if(actual[i] == predicted[i]):
            correct = correct + 1

    accuracy = ((correct/len(predicted))*100)
    print("total = " + str(len(predicted)))
    print("correct = " + str(correct))
    #print("accuracy = " + str(accuracy))

    new_accuracy = grading_metrics.accuracy_score(actual,predicted)
    print("accuracy = "+ str(new_accuracy))

    #f1_score = grading_metrics.f1_score(actual,predicted,average=None)
    f_score = grading_metrics.precision_recall_fscore_support(actual,predicted,average=None)
    print("\nprecision :" )
    class_index = 0
    for class_precision in f_score[0]:
        print("for class "+str(class_index+1) + " "+ str(class_precision))
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

    f1_score = grading_metrics.f1_score(actual,predicted,average=None)
    print("\nf1_measure :" )
    class_index = 0
    for class_f1 in f1_score:
        print("for class "+str(class_index+1) + " "+ str(class_f1))
        class_index+=1



