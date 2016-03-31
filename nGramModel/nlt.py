__author__ = 'sureshbvn'
from nltk.model import NgramModel
import nltk
from nltk.corpus import brown
from nltk.probability import LidstoneProbDist, WittenBellProbDist
from nltk.corpus import brown
from nltk import MLEProbDist
from nltk.probability import LidstoneProbDist, WittenBellProbDist

estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
fp=open("output.txt","r")
lines=fp.readlines()
fp.close()
#print lines

corpus=[]

for line in lines:
    splitLines= line.split()
    print splitLines
    for word in splitLines:
        if word !="":
            corpus.append(word)

print corpus
op="the rain in, spain falls mainly in the plains.This is a context. It has some generates a word hello world".split()
#lm = NgramModel(2, op,estimator=estimator)

lm = nltk.NgramModel(4, op, True,True,estimator)


# Thanks to miku, I fixed this problem

str="This is a context which generates a word"
print lm.prob("word", [str])

# But I got another program like this one...
print lm.prob("s", ["is to hell whats happening hh hsffdsf sfd "])

