# Restoring Casing and Punctuation in Spoken German Transcript

<h3>Introduction-</h3>
This approach aims to train a model using SVM classifier that classifies each token in the transcript into 5 classes
indicating the punctuation and capitalization as follows:
1. Class1 - First character is capital
2. Class2 - First character is capital and token is followed by period
3. Class3 - First character is capital and token is followed by comma
4. Class4 - Token is followed by period
5. Class5 - Token is followed by comma

<h5>Features:  
1. POS Tags(STTS Tags) : Using [Stanford German Tagger](http://nlp.stanford.edu/software/tagger.shtml)
2. Chunk Tags : Using [Tree Tagger](http://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/)
3. Word Features : Using [Word2Vec](https://radimrehurek.com/gensim/models/word2vec.html)

Classifier:
1. SVM Classifier - [BSVM](https://www.csie.ntu.edu.tw/~cjlin/bsvm/)

Tools: Install numpy, gensim, sklean, nltk, scipy for python
    
<h3>Datasource - Europarl: A Parallel Corpus for Statistical Machine Translation (German Language Version)-</h3>
1. [Europarl Dataset](http://www.statmt.org/europarl/)
2. Traininig Data - input.txt contains first 10,000 lines of Europarl Dataset German version
3. Testing Data - TestRaw.txt contains 10,001 to 13,000 lines 	
	 
<h3>Programs-</h3>
1. properties.py - set the paths for taggerJAR, training corpus, testing corpus, bsvm, tree tagger and all necessary files/models
2. generateWordVec.py - generates word vectors for the input corpus
3. tagging.py - generates pos-tags, chunk-tags and fetches word vectors for word2vec model 
4. features.py - generates feature vectors from the generated features
5. svm.py - takes in the generated feature vectors and trains the svm model, also runs the svm for classifying test data
5. test_data.py - generated test data from testing corpus
6. utility.py - contains data cleanining functions and other miscellaneous functions
7. evaluate.py - calculates overall accuracy, precision, recall and f1 measures for 5 classes
	