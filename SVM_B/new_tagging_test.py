# -*- coding: utf-8 -*-
from nltk.tag import StanfordPOSTagger
import utility as util
import sys
import os
import re
import properties
import gensim
import string as mstring


reload(sys)
sys.setdefaultencoding('utf-8')
tagger = properties.tagger
taggerJARPath = properties.taggerJARPath
st = StanfordPOSTagger(tagger,taggerJARPath)
chunkFile = properties.chunkTestFile
vectorModel = properties.vectorModel



def extractChunkTags():
        result = util.extract_All_Tags(chunkFile)
        chunktags = []
        for each in result:
            #if '$' in each:
            #    continue
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

def wordVectorModel():
     model = gensim.models.Word2Vec.load('save_word_model.txt')
     return model


def tree_tagger_preprocess(chunkTags):
    for i in range(len(chunkTags)-1):
        nextChunktag = chunkTags[i+1]
        if '.' in nextChunktag:
            chunkTags[i].append(".")
        elif ',' in nextChunktag:
            chunkTags[i].append(",")
        else:
            chunkTags[i].append("epsillon")
    chunkTags[len(chunkTags)-1].append("epsillon")

if __name__=="__main__":

    string = open("input_4.txt").read()
    cleaned_str = re.sub('[^a-zA-Z0-9\n\.\,\x7f-\xff]', ' ', string)
    cleaned_str = cleaned_str.replace('  ',' ').replace(' ,',',')
    vecModel = wordVectorModel()
    #postag_t = st.tag(cleaned_str.split())
    text_file = open(properties.test_tagged_output_file, "w")
    invokeChunker(cleaned_str)
    chunkTags = extractChunkTags()
    tree_tagger_preprocess(chunkTags)
    '''
    postag = []
    l = [',','...','.','\'','!','?','....',u'\xad',u'\xad,',u'\xad.']
    for i in range(len(postag_t)):
        if postag_t[i][0] not in l:
            postag.append(postag_t[i])
    '''
    # with open('listpostag.txt','w') as f:
    #     for i in postag:
    #         if i[0] == u'\xad' or i[0] == u'\xad,' or i[0] == u'\xad.':
    #             continue
    #         f.write(str(i)+'\n')
    # with open('listchunktag.txt','w') as f:
    #     for i in chunkTags:
    #         f.write(str(i)+'\n')

    for i in range(len(chunkTags)):
        tup = chunkTags[i]
        token = tup[0]
        tag = tup[1]


        chunkTag = chunkTags[i][3]
        nextchar = chunkTags[i][4]
        if nextchar is not "epsillon":
            token = token + nextchar

        if ',' in token[0] or '.' in token[0]:
            continue

        if token=="Freitag,":
            print "nonsense"

        if util.isCaptilized(token) and not (util.isCaptilizedwithPeriod(token) or util.isCaptilizedwithComma(token)) and nextchar=="epsillon":
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("0" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vecModel[util.cleanWordVec(tup[0]).strip().replace('.',"").replace(',',"").encode('utf-8')]).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        elif util.isCaptilizedwithPeriod(token) and nextchar==".":
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("1" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vecModel[util.cleanWordVec(tup[0]).strip().replace('.',"").replace(',',"").encode('utf-8')]).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        elif util.isCaptilizedwithComma(token) and nextchar==",":
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("2" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vecModel[util.cleanWordVec(tup[0]).strip().replace('.',"").replace(',',"").encode('utf-8')]).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        elif util.is_ending_withPeriod(token) and nextchar==".":
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("3" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vecModel[util.cleanWordVec(tup[0]).strip().replace('.',"").replace(',',"").encode('utf-8')]).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        elif util.is_ending_withComma(token) and nextchar==",":
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("4" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vecModel[util.cleanWordVec(tup[0]).strip().replace('.',"").replace(',',"").encode('utf-8')]).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

        else:
            #print tup[0].encode('utf=8') +"   " + util.cleanWordVec(tup[0])
            text_file.write("5" + " "+tup[0]+" "+tup[1]+" "+chunkTag+" "+str(vecModel[util.cleanWordVec(tup[0]).strip().replace('.',"").replace(',',"").encode('utf-8')]).replace("\n","").replace('[',"").replace(']',"").strip()+"\n")

    text_file.close()

