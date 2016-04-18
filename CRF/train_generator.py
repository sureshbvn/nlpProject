import os

dictionary = {",":'COMMA',".":'PERIOD'}
dictionary1 = {",":'CAP_COMMA',".":'CAP_PERIOD'}

fo = open('outEuropal.txt')
data = fo.read()
fo.close()
data = data.split('\n')
print len(data)

data = data[:1308460]
#data = data[130846:156980]
#print data[-3]

fw = open('data/train.txt','w')

#final = []
for i in range(len(data)-1):
	temp = data[i].split('\t')
	st = ""
	if temp[1][0]=='$':
		continue
	punct = data[i+1].split('\t')
	temp[2] = temp[2].strip()
#	print temp,punct
#	print temp[0]
	if temp[0][0]<='Z' and temp[0][0]>='A':
#		print 'here'
		if punct[1][0]=='$' and temp[1][0]!='$':
			st = (temp[0],temp[1],temp[2],dictionary1.get(punct[0],'CAP'))
		if punct[1][0]!='$':
			st = (temp[0],temp[1],temp[2],'CAP')	
	elif punct[1][0]=='$' and temp[1][0]!='$':
		st = (temp[0],temp[1],temp[2],dictionary.get(punct[0],'EPSILON'))
	elif punct[1][0]!='$':
		st = (temp[0],temp[1],temp[2],'EPSILON')

	fw.write(st[0].lower())
	fw.write('\t')
	fw.write(st[1].lower())
	fw.write('\t')
	fw.write(st[2].lower())
	fw.write('\t')
	fw.write(st[3].lower())
	fw.write('\n')
		
#temp = data[-1].split('\t')
#if temp[1][0]!='$':
#	st = (temp[0],temp[1],'EPSILON')
#	final.append(st)
	
#print 'Number of tokens ',len(final)
#print final[-1]
#fw = open('euro_train.txt','w')
#for i in range(len(final)):
#	print len(final[i])
#	print final[i]
#	fw.write(final[i][0])
#	fw.write('\t')
#	fw.write(final[i][1])
#	fw.write('\t')
#	fw.write(final[i][2])
#	fw.write('\t')
#	fw.write(final[i][3])
#	fw.write('\n')
	
fw.close()


#print len(final)
##print final[-1]
#fw = open('euro_test_file.txt','w')
#for i in range(len(final)):
#	print len(final[i])
#	print final[i]
#	fw.write(final[i][0])
#	fw.write('\t')
#	fw.write(final[i][1])
#	fw.write('\n')
#	
#fw.close()
