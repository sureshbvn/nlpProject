from nltk.tag.stanford import StanfordPOSTagger
import nltk
import os

os.environ['CLASSPATH'] = "/home/vishesh/Downloads/stanford-postagger-full-2015-12-09/"

english_postagger = StanfordPOSTagger('models/english-bidirectional-distsim.tagger')

print english_postagger.tag(nltk.word_tokenize('this is stanford postagger in nltk for python users'))


fo = open('europarl-v7.de-en.de','r')
data = fo.read()
fo.close()

fw = open('europarl_tags_testing.txt','w')

data = data.decode('utf-8')
data = data.split('\n')

#tokens = data.split()
#print len(tokens)

#print 'Tagging...'

german_postagger = StanfordPOSTagger('/home/vishesh/Documents/NLP/postagger/models/german-fast-caseless.tagger')
for i in range(10000,11500):
	tokens = nltk.word_tokenize(data[i])
	
	tags = german_postagger.tag(tokens)

#	print len(tags)
	if i%1000==0:
		print i

	for j in range(len(tags)):
		fw.write(tags[j][0].encode('utf-8'))
		fw.write('\t')
		fw.write(tags[j][1].encode('utf-8'))
		fw.write('\n')
		
fw.close()
