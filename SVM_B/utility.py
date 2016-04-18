# -*- coding: utf-8 -*-
import re

def isCaptilized(word):
    if word[0].isupper():
         return True
    return False

def isCaptilizedwithPeriod(word):
    if isCaptilized(word):
        if word.endswith('.') :
            return True
    return False

def isCaptilizedwithComma(word):
    if isCaptilized(word):
        if word.endswith(',') :
            return True
    return False

def is_ending_withPeriod(word):
    if not isCaptilized(word):
        if word.endswith('.'):
            return True
        return False

def is_ending_withComma(word):
    if not isCaptilized(word):
        if word.endswith(','):
            return True
        return False

def extract_All_Tags(chunkFile):

    result = []
    with open(chunkFile, 'r') as f:
        flag = 0
        ctag = 0
        result = []
        for line in f:
            line = line[:-1]
            if line == "<NC>" or line == "<PC>" or line == "<VC>":
                flag=1
                ctag = line[1:-1]
                continue
            elif line == "</NC>" or line == "</PC>" or line == "</VC>":
                ctag = ""
                #flag = 0
                continue
            elif flag==1:
                if "$" not in line:
                    newline = line+" "+ctag
                    result.append(newline)
                else:
                    newline = line
                    result.append(newline)
    f.close()
    return result

def cleanWordVec(text):
    if text == 'D�ez':
        print 4
    cleanTxt = re.sub('[^a-zA-Z0-9\n\\x7f-\xff\d+\.\d+\d+,\d+]', ' ', text)
    cleanTxt = cleanTxt.lower()
    # Dealing with the German umlauts (might still be capitalized) and sharp s
    cleanTxt = cleanTxt.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    cleanTxt = cleanTxt.replace('Ä', 'ae').replace('Ö', 'oe').replace('Ü', 'ue')
    # Strip the most frequent accents from foreign words
    cleanTxt = cleanTxt.replace('é', 'e').replace('è', 'e').replace('á', 'a').replace('à', 'a')
    cleanTxt = cleanTxt.replace('É', 'e').replace('È', 'e').replace('Á', 'a').replace('À', 'a')
    cleanTxt = cleanTxt.replace('í', 'i').replace('ì', 'i').replace('Í', 'i').replace('Ì', 'i')
    cleanTxt = cleanTxt.replace('ó', 'o').replace('ò', 'o').replace('Ó', 'o').replace('Ò', 'o')
    cleanTxt = cleanTxt.replace('œ', 'oe').replace('Œ', 'oe').replace('â', 'a').replace('Â', 'a')
    cleanTxt = cleanTxt.replace('ñ', 'n').replace('ç', 'c').replace('ø', 'o').replace('å', 'a')
    cleanTxt = cleanTxt.replace('º','')
    # Stripping all non alphabetical or numerical tokens that are left (mainly punctuation)
    #cleanTxt = re.sub('[^a-z1-9 ]', '', cleanTxt)
    return cleanTxt

def getListWordVec(text):
    listOfSentence = text.split("\n")

    resultList = []
    for each in listOfSentence:
        each = each.replace("  "," ")
        temp1 = each.split(" ")
        temp2 =[]
        for eachWord in temp1:
            temp2.append(eachWord.strip())
        resultList.append(temp2)
    return  resultList
