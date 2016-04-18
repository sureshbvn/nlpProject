import sys

dictionary = {"epsilon":0,"cap":1,"comma":2,"cap_comma":3,"period":4,"cap_period":5}

#fo = open('/home/vishesh/Documents/NLP/postagger/europarl-v7.de-en.de','r')
#lines = fo.readlines()
#fo.close()
fw = open('data/data.txt','w')
#for i in range(4000):
#	fw.write(lines[i])

#words = lines[3999].split()
#w1 = words[-2]
#w2 = words[-1][:-1]
#print w1,w2
#fw.close()

fo = open('data/tags.txt','r')
lines = fo.readlines()
fo.close()
fw = open('data/labels.txt','w')
fw2 = open('data/text.txt','w')
#w1 = w1.lower()
#w2 = w2.lower()

st = ""
y = []
for i in range(1,len(lines)):
	text1 = lines[i-1].split()
	text2 = lines[i].split()
#	if w1 in text1[0] and w2 in text2[0]:
#		y.append(dictionary.get(text2[-1]))
#		st += text2[0]+'\n'
#		break
#	else:
	y.append(dictionary.get(text2[-1]))
	st += text1[0]+'\n'
print i
for i in range(len(y)):
	fw.write(str(y[i]))
	fw.write('\n')
	
fw.close()


fw2.write(st)
fw2.close()
