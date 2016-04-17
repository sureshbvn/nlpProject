# -*- coding: utf-8 -*-
from nltk.tag import StanfordPOSTagger
import utility as util
import sys
import os
import re
import properties
import gensim

reload(sys)
sys.setdefaultencoding('utf-8')
tagger = properties.tagger
taggerJARPath = properties.taggerJARPath
chunkFile = properties.chunkTestFile
st = StanfordPOSTagger(tagger,taggerJARPath)
l = ['...,',',','...','.','\'','!','?','....',u'\xad',u'\xad,',u'\xad.']

def extractChunkTags():
        result = util.extract_All_Tags(chunkFile)
        chunktags = []
        for each in result:
            if '$' in each:
                continue
            temp1 = each.split("\t")
            temp2 = temp1[2].split()
            if len(temp2) == 1:
                temp2.append('XX')
            temp3 = []
            temp3.append(temp1[0])
            temp3.append(temp1[1])
            temp3.append(temp2[0])
            temp3.append(temp2[1])
            chunktags.append(temp3)
        return chunktags


def wordVectorModel(cleaned_str):
     trainingText = util.cleanWordVec(cleaned_str)
     trainingTextInput = util.getListWordVec(trainingText)
     model = gensim.models.Word2Vec(trainingTextInput,size = 5,min_count = 1)
     return model

def invokeChunker(cleanInput):

    with open(properties.chunkTestTemp, 'w') as f:
        f.write(cleanInput)
        f.close()
    fullPath = properties.chunkTestTemp
    chunkerPath = properties.chunker_path
    attr = "chunk-german"
    config = " > "+str(chunkFile)
    cmd = chunkerPath+"\\"+attr+" "+fullPath+ config
    print cmd
    os.system(cmd)


def classLabel(str):
    resultList = []
    for token in str:
         if token not in l:
            temp = []
            if util.isCaptilized(token) and not (util.isCaptilizedwithPeriod(token) or util.isCaptilizedwithComma(token)):
                temp.append(token)
                temp.append(0)
            elif util.isCaptilizedwithPeriod(token):
                temp.append(token)
                temp.append(1)
            elif util.isCaptilizedwithComma(token):
                temp.append(token)
                temp.append(2)
            elif util.is_ending_withPeriod(token):
                temp.append(token)
                temp.append(3)
            elif util.is_ending_withComma(token):
                temp.append(token)
                temp.append(4)
            else:
                temp.append(token)
                temp.append(5)
            resultList.append(temp)
    return resultList



if __name__=="__main__":

    string = open(properties.test_raw).read()
    cleaned_str = util.pretestDataTransformations(string)
    resultList = classLabel(cleaned_str.split())
    cleaned_test_str = util.testDataTransformations(string)

    postag_t = st.tag(cleaned_test_str.split())
    text_file = open(properties.test_tagged_output_file, "w")
    invokeChunker(cleaned_test_str)
    chunkTags = extractChunkTags()

    vecModel = gensim.models.Word2Vec.load(properties.word_vec_model)

    postag = []
    for i in range(len(postag_t)):
        if postag_t[i][0] not in l:
            postag.append(postag_t[i])

    # with open('TESTING.txt','w') as f:
    #  for i in range(len(resultList)):
    #     f.write(str(i)+" "+str(resultList[i][0])+" "+str(postag[i][0])+" "+chunkTags[i][0]+"\n")

    print 'generating test features...\n'
    for i in range(len(postag)):
        #print i
        tup = postag[i]
        token = tup[0]
        tag = tup[1]
        chunkTag = chunkTags[i][3]
        wordVecInput = util.makeWordVecTransformations(token)
        wordVecInput = util.cleanWordVec(wordVecInput)

        if util.cleanWordVec(wordVecInput).strip().encode('utf-8') in  vecModel:
            vector = vecModel[util.cleanWordVec(wordVecInput).strip().encode('utf-8')]
        else:
            print 5
            vector = '[0 0 0 0 0]'

        if (str(postag[i][0]).replace('.','').replace(',','')) != ((str(chunkTags[i][0])).replace('.','').replace(',','')):
            print 4

        text_file.write(str(resultList[i][1])+" "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vector).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

    text_file.close()
    print 'generating test features finished\n'

