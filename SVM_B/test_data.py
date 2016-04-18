# -*- coding: utf-8 -*-
from nltk.tag import StanfordPOSTagger
import utility as util
import sys
import os
import re
import properties

reload(sys)
sys.setdefaultencoding('utf-8')
tagger = properties.tagger
taggerJARPath = properties.taggerJARPath
chunkFile = properties.chunkTestFile
st = StanfordPOSTagger(tagger,taggerJARPath)


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
      if not (token == ',' or token == '.'):
        if util.isCaptilized(token) and not (util.isCaptilizedwithPeriod(token) or util.isCaptilizedwithComma(token)):
            resultList.append(0)
        elif util.isCaptilizedwithPeriod(token):
            resultList.append(1)
        elif util.isCaptilizedwithComma(token):
            resultList.append(2)
        elif util.is_ending_withPeriod(token):
            resultList.append(3)
        elif util.is_ending_withComma(token):
            resultList.append(4)
        else:
            resultList.append(5)
    return resultList



if __name__=="__main__":

    string = open(properties.test_raw).read()
    str_ = re.sub('[^a-zA-Z0-9\n\.\,\x7f-\xff]', ' ', string)
    resultList = classLabel(str_.split())
    cleaned_test_str = re.sub('[^a-zA-Z0-9\n\x7f-\xff]', ' ', string).lower()
    postag_t = st.tag(cleaned_test_str.split())
    text_file = open(properties.test_tagged_output_file, "w")
    invokeChunker(cleaned_test_str)
    chunkTags = extractChunkTags()

    postag = []
    l = [',','...','.','\'','!']
    for i in range(len(postag_t)):
        if postag_t[i][0] not in l:
            postag.append(postag_t[i])

    for i in range(len(postag)):
        tup = postag[i]
        token = tup[0]
        tag = tup[1]
        chunkTag = chunkTags[i][3]
        text_file.write(str(resultList[i])+" "+tup[0]+" "+tup[1]+" "+chunkTag+"\n")


    text_file.close()

