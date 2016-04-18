import keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout,TimeDistributedDense
from keras.layers.recurrent import LSTM
from keras.preprocessing import text,sequence
from keras.layers.embeddings import Embedding
from keras.utils import np_utils
from sklearn.cross_validation import train_test_split
import numpy as np

base_filter = "\n"

fo = open('data/text.txt','r')
text = fo.readlines()
fo.close()
print 'Number of lines ',len(text)

#dec = {}
#for i in range(len(text)):
#	dec[text[i]] = 1
#print len(dec)
#raw_input("Stop")

st = ""
for i in range(len(text)):
	st += text[i]

fo = open('data/labels.txt','r')
labels = fo.readlines()
fo.close()
y = []
for i in range(len(labels)):
	y.append(int(labels[i]))
print 'Number of labels ',len(y)



#Size of Vocabulary
n = 50000
#Max size of an input sequence
maxlen = 10

X_data = keras.preprocessing.text.one_hot(st, n,filters=base_filter, lower=True, split=" ")

print 'X_data ',len(X_data)

Y_train = np_utils.to_categorical(y, 6)
#X_data,X_test,Y_train,Y_test = train_test_split(X_data,Y_train,test_size=0.15,random_state=55)

for i in range(7):
	Y_train = np.vstack([Y_train,[1,0,0,0,0,0]])
i=0
new_list = np.expand_dims(Y_train[i:i+10],axis=0)
print new_list.shape
i+=10
while i<len(X_data):
  if i%100000==0:
  	print i
#  tmp = np.expand_dims(Y_train[i:i+10],axis=0)
#  new_list = np.vstack([new_list,tmp])
  i+=10

Y_train = new_list
print 'New Y Train ',Y_train.shape

i=0
new_list=[]
while i<len(X_data):
  new_list.append(X_data[i:i+10])
  i+=10

X_train = keras.preprocessing.sequence.pad_sequences(new_list, maxlen=maxlen, dtype='int32')

X_back = X_train
Y_back = Y_train
X_train = X_back[:100000]
Y_train = Y_back[:100000]
X_test = X_back[100000:]
Y_test = Y_back[100000:]

print X_train.shape
print Y_train.shape
#i=0
#test_list=[]
#while i<len(X_test):
#  test_list.append(X_test[i:i+10])
#  i+=10

#X_test = keras.preprocessing.sequence.pad_sequences(test_list, maxlen=maxlen, dtype='int32')


#for i in range(4):
#	Y_test = np.vstack([Y_test,[1,0,0,0,0,0]])
#i=0
#new_list = np.expand_dims(Y_test[i:i+10],axis=0)
#print new_list.shape
#i+=10
#while i<len(Y_test):
#  tmp = np.expand_dims(Y_test[i:i+10],axis=0)
#  new_list = np.vstack([new_list,tmp])
#  i+=10

#Y_test = new_list
#print 'New Y Test ',Y_test.shape


print X_test.shape
print Y_test.shape

np.save('data/X_train.npy',X_train)
#np.save('data/Y_train.npy',Y_train)
np.save('data/X_test.npy',X_test)
#np.save('dataY_test.npy',Y_test)

raw_input('Stop')

#X_train = np.expand_dims(X_train,axis=-1)

model = Sequential()
model.add(Embedding(16000, 64, input_length=10))

model.add(LSTM(32, input_shape=(10,64),return_sequences=True))
model.add(TimeDistributedDense(6,activation='softmax'))

sgd = keras.optimizers.SGD(lr=0.0001, decay=1e-6, momentum=0.9, nesterov=False)

model.compile(loss='categorical_crossentropy', optimizer='adadelta')
model.fit(X_train, Y_train, batch_size=128, nb_epoch=20,show_accuracy=True,validation_data=(X_test, Y_test))
#model.load_weights('train_1.0.npy')

trscore = model.evaluate(X_train, Y_train, show_accuracy=True,verbose=2)
print('Train score: ', trscore[0])
print('Train accuracy: ', trscore[1])
trscore = model.evaluate(X_test, Y_test, show_accuracy=True,verbose=2)
print('Test score: ', trscore[0])
print('Test accuracy: ', trscore[1])


arr = model.predict_classes(X_test, batch_size=128, verbose=1)

model.save_weights('train_1.0.npy')

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

for i in range(Y_test.shape[0]):
	for j in range(Y_test.shape[1]):
		tmp = np.argmax(Y_test[i][j])
		actual[tmp]+=1
		if tmp==arr[i][j]:
			correct[arr[i][j]]+=1
		
print 'Correct ',correct
print 'Actual ',actual
