import sys

dictionary = {"cap":0,"cap_comma":1,"cap_period":2,"comma":3,"epsilon":4,"period":5}

#path1 = sys.argv[1]

fo = open('data/test.txt','r')
test = fo.read()
fo.close()

fo2 = open('data/output.txt','r')
truth = fo2.read()
fo2.close()

test = test.split('\n')
truth = truth.split('\n')


count = 0 
print len(test)
print len(truth)
for i in range(len(test)-2):
	t1 = test[i].split('\t')
#	print t1
	if t1[-1]=='EPSILON' or t1[-1]=='Epsilon' or t1[-1]=='epsilon':
		count+=1

print count
print 'Baseline Accuracy: ',float(count)/float(len(truth))


count = 0 
for i in range(len(test)-2):
	t1 = test[i].split('\t')
	t2 = truth[i].split('\t')
#	print t1,t2
	if t1[0]!=t2[0]:
		print i
		break
	
	if t1[-1]==t2[-1]:
		count+=1
		
print count
print 'Accuracy: ',float(count)/float(len(test))


print '\n\nFor Individual Classes'



correct = [0,0,0,0,0,0]
total = [0,0,0,0,0,0]
fn = [0,0,0,0,0,0]
fp = [0,0,0,0,0,0]
tn = [0,0,0,0,0,0]
tp = [0,0,0,0,0,0]

for i in range(len(test)-2):
	t1 = test[i].split()
	t2 = truth[i].split()
	total[dictionary.get(t1[-1])]+=1
	if t1[-1]==t2[-1]:
		correct[dictionary.get(t1[-1])]+=1

keys = dictionary.keys()
list.sort(keys)
print keys
for i in range(len(keys)):
	key = keys[i]
	for j in range(len(test)-2):
		t1 = test[j].split()
		t2 = truth[j].split()
		if t1[-1]!=t2[-1]:
			if t1[-1]==key:
				fn[dictionary[key]]+=1
			elif t2[-1]==key:
				fp[dictionary[key]]+=1
		elif t1[-1]==t2[-1] and t1[-1]!=key:
			tn[dictionary[key]]+=1			
		elif t1[-1]==t2[-1] and t2[-1]==key:
			tp[dictionary[key]]+=1
	
print 'False Positive ',fp
print 'False Negative ',fn
print 'True Negative ',tn	
print 'True Positive ',tp
print 'Correct ',correct
print total 
acc = [0.0,0.0,0.0,0.0,0.0,0.0]
pre = [0.0,0.0,0.0,0.0,0.0,0.0]
rec = [0.0,0.0,0.0,0.0,0.0,0.0]
f1 = [0.0,0.0,0.0,0.0,0.0,0.0]

for i in range(len(correct)):
	acc[i] = float(correct[i])/float(total[i])
	acc[i]*=100
	
	pre[i] = float(tp[i])/float(tp[i]+fp[i])
	rec[i] = float(tp[i])/float(tp[i]+fn[i])
	f1[i] = float(2*pre[i]*rec[i])/float(pre[i]+rec[i]) 
	pre[i]*=100
	rec[i]*=100
	f1[i]*=100

f1_av = 0.0	
st=""
for i in range(len(keys)):
	if i>=1 and i<3:
		st += keys[i]+'\t'
	else:
		st += keys[i]+'\t\t'
print st
st=""
for i in range(len(acc)):
	st += str('{0:.5f}'.format(acc[i]))+'\t'
print st
st=""
for i in range(len(acc)):
	st += str('{0:.5f}'.format(pre[i]))+'\t'
print st
st=""
for i in range(len(acc)):
	st += str('{0:.5f}'.format(rec[i]))+'\t'
print st
st=""
for i in range(len(acc)):
	st += str('{0:.5f}'.format(f1[i]))+'\t'
	f1_av += f1[i]
print st
	
	
print 'Average F1: ',f1_av/len(f1)
