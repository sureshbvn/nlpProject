[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/desilinguist/swig-srilm/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

### Ngram Based Punctuation Restoration
==========

#### Description
================
Steps Involved:
1)Pre process the training data to change all the "," to ",COMMA" and all the periods "." to ".PERIOD". 

2)Create all possible n-grams from the training data. The n value can be dynamic. But the n value chosen for experimenting is 4.

3)The model file is created which contains the probablity of Word given context.

4)The test data is an output of ASR data. The current format which is used is all lower case strings with no punctations. 

5)The smoothing technique used is Stupid Backoff. The module restores the puncations on test data.


#### Requirements
- GNU make
- Simplified Wrapper & Interface Generator ([SWIG](http://swig.org/)) 
- A local Python and/or Perl installation
- The SRILM toolkit (v1.7.1). If you have an older version of SRILM e.g., the 1.5.x series then you should use the `old_srilm` branch. Note that SRILM should have been compiled as position independent code. You can do that by using the command `MAKE_PIC=yes make` when compiling SRILM.

*IMPORTANT*: This code has been extensively tested on x86-64 machines running Linux. 
#### Installation:
Copy `_srilm.so` and `srilm.py` to your directory where you want to 
use the python module. You can run the included `test.py` script to check 
whether the compiled module works correctly. The output of test.py should be
the following:
```
1. Number of n-grams:
   There are 11868 unigrams in this LM
   There are 59481 bigrams in this LM
   There are 16744 trigrams in this LM
   There are 13787 4-grams in this LM
   There are 12082 5-grams in this LM

2. N-gram log probabilities:
   p('good') = -3.49373698235
   p('of the') = -0.558740794659
   p('nitin madnani') = -99.0
   p('there are some') = -0.985605716705
   p('do more about your') = -0.469523012638
   p('or whatever has yet to') = -0.53226429224

3. Sentence log probabilities and perplexities:
   p('there are some good') = -9.85836982727
   ppl('there are some good') = 93.6858444214

4. OOvs:
   nOOVs('there are some foobar') = 1

5. Corpus log probabilties and perplexities:
   Logprob for the file test.txt = -33.6016654968
   Perplexity for the file test.txt = 94.7476806641
```
- To create a Perl module, run `make perl` in this directory. 
Copy `srilm.so` and `srilm.pm` to the directory of your choice. 
Run the included Perl script 'test.pl' to test whether the compiled module works correctly.
The output should be the same as above.


 


