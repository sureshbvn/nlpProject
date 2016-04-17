# -*- coding: utf-8 -*-
from nltk.tag import StanfordPOSTagger
import utility as util
import sys
import os
import properties
import gensim
import re



reload(sys)
sys.setdefaultencoding('utf-8')
tagger = properties.tagger
taggerJARPath = properties.taggerJARPath
st = StanfordPOSTagger(tagger,taggerJARPath)
chunkFile = properties.chunkFile



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

    with open(properties.chunkTemp, 'w') as f:
        f.write(cleanInput)
        f.close()
    fullPath = properties.chunkTemp
    chunkerPath = properties.chunker_path
    attr = "chunk-german"
    config = " > "+str(chunkFile)
    cmd = chunkerPath+"\\"+attr+" "+fullPath+ config
    print cmd
    os.system(cmd)

if __name__=="__main__":

    string = open(properties.input_corpus_file).read()
    cleaned_str = util.makeTaggingTransformations(string)
    vecModel = gensim.models.Word2Vec.load(properties.word_vec_model)
    postag_t = st.tag(cleaned_str.split())
    text_file = open(properties.tagged_output_file, "w")
    invokeChunker(cleaned_str)
    chunkTags = extractChunkTags()

    postag = []
    l = ['...,',',','...','.','\'','!','?','....',u'\xad',u'\xad,',u'\xad.']
    for i in range(len(postag_t)):
        if postag_t[i][0] not in l:
            postag.append(postag_t[i])

    # with open('listpostag.txt','w') as f:
    #     for i in postag:
    #         if i[0] == u'\xad' or i[0] == u'\xad,' or i[0] == u'\xad.':
    #             continue
    #         f.write(str(i)+'\n')
    # with open('listchunktag.txt','w') as f:
    #     for i in chunkTags:
    #         f.write(str(i)+'\n')

    print 'generating features...\n'
    for i in range(len(postag)):
        tup = postag[i]
        token = tup[0]
        tag = tup[1]
        wordVecInput = util.makeWordVecTransformations(token)
        wordVecInput = util.cleanWordVec(wordVecInput)
        if util.cleanWordVec(wordVecInput).strip().encode('utf-8') in  vecModel:
            vector = vecModel[util.cleanWordVec(wordVecInput).strip().encode('utf-8')]
        else:
            vector = '[0 0 0 0 0]'
        if (str(postag[i][0]).replace('.','').replace(',','')) != ((str(chunkTags[i][0])).replace('.','').replace(',','')):
            print 4

        chunkTag = chunkTags[i][3]
        if util.isCaptilized(token) and not (util.isCaptilizedwithPeriod(token) or util.isCaptilizedwithComma(token)):
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("0" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vector).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        elif util.isCaptilizedwithPeriod(token):
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("1" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vector).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        elif util.isCaptilizedwithComma(token):
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("2" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vector).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        elif util.is_ending_withPeriod(token):
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("3" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vector).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        elif util.is_ending_withComma(token):
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("4" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vector).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        else:
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("5" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vector).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

    text_file.close()
    print 'generating features finished\n'

