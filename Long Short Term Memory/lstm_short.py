import keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout,TimeDistributedDense
from keras.layers.recurrent import LSTM
from keras.preprocessing import text,sequence
from keras.layers.embeddings import Embedding
from keras.utils import np_utils
from sklearn.cross_validation import train_test_split
import numpy as np
from keras.regularizers import l2, activity_l2

dictionary = {"epsilon":0,"cap":1,"comma":2,"cap_comma":3,"period":4,"cap_period":5}

#Size of Vocabulary
n = 50000
#Max size of an input sequence
maxlen = 10

X_train = np.load('data/X_train.npy')
Y_train = np.load('data/Y_train.npy')
X_test = np.load('data/X_test.npy')
Y_test = np.load('data/Y_test.npy')

print 'Train data ',X_train.shape
print 'Train labels ',Y_train.shape
print 'Test data ',X_test.shape
print 'Test labels ',Y_test.shape


model = Sequential()
model.add(Embedding(50000, 256, input_length=10))

model.add(LSTM(128, input_shape=(10,256),return_sequences=True))
model.add(TimeDistributedDense(6,activation='softmax'))

sgd = keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=False)

model.compile(loss='categorical_crossentropy', optimizer=sgd)

#model.load_weights('models/train_50000vocab.npy')

model.fit(X_train, Y_train, batch_size=128, nb_epoch=30,show_accuracy=True,validation_data=(X_test, Y_test))


trscore = model.evaluate(X_train, Y_train, show_accuracy=True,verbose=2)
print('Train score: ', trscore[0])
print('Train accuracy: ', trscore[1])
trscore = model.evaluate(X_test, Y_test, show_accuracy=True,verbose=2)
print('Test score: ', trscore[0])
print('Test accuracy: ', trscore[1])


arr = model.predict_classes(X_test, batch_size=128, verbose=1)

print len(arr)
#out = []
#for i in range(len(arr)):
#	for j in range(len(arr[i])):
#		out.append(arr[i][j])

#print len(out)
print Y_test.shape
count = 0
total = 0
for i in range(Y_test.shape[0]):
	for j in range(Y_test.shape[1]):
		total+=1
		tmp = np.argmax(Y_test[i][j])
		if tmp==arr[i][j]:
			count+=1
		
print 'Correct ',count
print 'Total ',total
print 'Accuracy ',float(count)/float(total)


correct = [0,0,0,0,0,0]
actual = [0,0,0,0,0,0]
false_negative = [0,0,0,0,0,0]
false_positive = [0,0,0,0,0,0]
pre = [0.0,0.0,0.0,0.0,0.0,0.0]
rec = [0.0,0.0,0.0,0.0,0.0,0.0] 
f1 = [0.0,0.0,0.0,0.0,0.0,0.0]

for i in range(Y_test.shape[0]):
	for j in range(Y_test.shape[1]):
		tmp = np.argmax(Y_test[i][j])
		actual[tmp]+=1
		if tmp==arr[i][j]:
			correct[arr[i][j]]+=1
		else:
			false_negative[tmp]+=1
			false_positive[arr[i][j]]+=1
		
		
print dictionary.keys()
print 'True Positive ',correct
print 'Total ',actual
print 'False Negative ',false_negative
print 'False Positive ',false_positive
for i in range(6):
	pre[i] = float(correct[i])/float(correct[i]+false_positive[i]) 
	rec[i] = float(correct[i])/float(correct[i]+false_negative[i])
	f1[i] = float(2*pre[i]*rec[i])/float(pre[i]+rec[i])
	
print 'Precision ',pre
print 'Recall ',rec
print 'F1 ',f1
f1_average = 0.0
for i in range(6):
	f1_average += f1[i]
print 'Average F1 Score ',f1_average/6

model.save_weights('models/train_50000vocab_sgd.npy')
