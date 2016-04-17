# -*- coding: utf-8 -*-
import properties
import gensim
import utility as util
import sys

reload(sys)
sys.setdefaultencoding('utf-8')




def wordVectorModel(cleaned_str):
     trainingText = util.cleanWordVec(cleaned_str)
     trainingTextInput = util.getListWordVec(trainingText)
     model = gensim.models.Word2Vec(trainingTextInput,size = 5,min_count = 1)
     model.save(properties.word_vec_model)

if __name__=="__main__":

    string = open(properties.word_vec_train_file).read()
    clean_str = util.makeWordVecTransformations(string)
    vecModel = wordVectorModel(clean_str)

