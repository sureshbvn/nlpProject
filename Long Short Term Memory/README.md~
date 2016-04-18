# Using LSTM for Restoring Casing and Punctuation in Spoken German Transcript

<h3> Introduction </h3>
The current model uses 1.1 million tokens as training data and 15,000 testing tokens. We use the previous context of a word 10 timesteps in the past or we look at 10 words in the past for gathering context information. The vocabulary size used for generating vector representations of the input is 50,000. 
<br>
The results of the training procedure on the data:<br>
Total Accuracy: 83.78%<br>
Average F1 Score: 45.52%
<br>
The classification task is:<br>
1. Class 1 - First character is capital F1-score:83.23%<br>
2. Class 2 - First character is capital and token is followed by period F1-score:0.0%<br>
3. Class 3 - First character is capital and token is followed by comma F1-score:18.58%<br>
4. Class 4 - Token is followed by period F1-score:40.43%<br>
5. Class 5 - Token is followed by comma F1-score:39.85%<br>
6. Class 6 - No Change 91.04%<br>

Features:  
1. Word Features : Using [[Word Embeddings]](http://arxiv.org/abs/1512.05287)

Libraries Used:
1. [[Keras]](https://github.com/fchollet/keras) - A Python wrapper on Theano Deep Learning library

Tools: numpy, keras, theano, scipy, sklearn
    
<h3> Datasource - Europarl: A Parallel Corpus for Statistical Machine Translation (German Language Version)</h3>
1. [[Europarl Dataset]](http://www.statmt.org/europarl/)
2. Traininig Data - X_train.npy & Y_train.npy contains first 50,000 lines of Europarl Dataset German version
3. Testing Data - X_test.npy & Y_test.npy contains line numbers 50,000 to 60,000 from the same dataset 	
	 
<h3> Programs </h3>
1. lstm_short.py - the lstm model takes training and testing numpy files and trains the model on that data
2. lstm.py - Generates word vectors and creates starting and ending markers for tokens at an interval of 10 tokens
3. lstm_data.py - Extracts the output labels and the word tokens given as input to lstm.py from the file tags.txt
	
	
	
