import itertools
from srilm import *
import string
from clean_test_corpus import Clean


class NgramTest:
    def __init__(self, model_file, test_file):
        self.model_file = model_file
        self.test_file = test_file
        self.puncationlist = ["espsilon", ",COMMA", ".PERIOD"]
        self.n = initLM(4)
        self.fw=open("output.txt","w+")

    def length_of_sentence(self, sentence):
        count = len(sentence.split())
        return count

    def create_combinations(self, bigram):
        list1 = [bigram[0]]
        list1.append(bigram[1])
        list1.extend(self.puncationlist)
        combination_list = list(itertools.permutations(list1))
        #print combination_list

    def get_probability(self, ngram):

        length = self.length_of_sentence(ngram)


        if length>5:
            raise ValueError('The n value specified is greater than 5')
        p6 = getNgramProb(self.n, ngram,length)
        #p6 = getSentenceProb(self.n, ngram, length)
        print ngram
        print p6
        return p6



    def max_in_list(self,prob_list):

        maxValue=-9999999.0000000
        for key in prob_list.keys():
            floatvalue=key

            if floatvalue>maxValue:
                maxValue=floatvalue

        if maxValue>=0:

            raise ValueError('The prob vallues are not correct')


        return maxValue







    def punctuate(self,string_list):

        #print string_list

        string11=str(string_list[0]+" "+",COMMA"+" "+string_list[1]+" .PERIOD")


        string21 = str(string_list[0] + " " + ".PERIOD" + " " + string_list[1] + " ,COMMA")

        string31 = str(string_list[0] + " " + "epsilon " + string_list[1] + " .PERIOD")

        string41 = str(string_list[0] + " " + ",COMMA" + " " + string_list[1]+" "+"epsilon ")

        string5 = str(string_list[0] + " " + "epsilon "+ string_list[1] + " ,COMMA")

        string6 = str(string_list[0] + " " + ".PERIOD" + " " + string_list[1]+" "+"epsilon")

        string7 = str(string_list[0] + " "+"epsilon " + string_list[1]+" epsilon")

        string8 = str(string_list[0] + " " + ".PERIOD " + string_list[1] + " .PERIOD")

        string9 = str(string_list[0] + " " + ",COMMA " + string_list[1] + " ,COMMA")




        prob11=ngram.get_probability(string11)


        prob21 = ngram.get_probability(string21)


        prob31 = ngram.get_probability(string31)


        prob41 = ngram.get_probability(string41)



        prob5 = ngram.get_probability(string5)
        prob6 = ngram.get_probability(string6)
        prob7 = ngram.get_probability(string7)
        prob8 = ngram.get_probability(string8)
        prob9 = ngram.get_probability(string9)

        prob_list={}
        prob_list[float(prob11)]=string11



        prob_list[float(prob21)] = string21


        prob_list[float(prob31)] = string31


        prob_list[float(prob41)] = string41


        prob_list[float(prob5)] = string5
        prob_list[float(prob6)] = string6
        prob_list[float(prob7)] = string7
        prob_list[float(prob8)] = string8
        prob_list[float(prob9)] = string9
        #print prob_list

        maxValue=self.max_in_list(prob_list)
        print maxValue
        return prob_list[maxValue]












        '''

        ngram.get_probability("Niederlage ,COMMA Deutschlands .PERIOD")
        ngram.get_probability("Niederlage Deutschlands")
        ngram.get_probability("Niederlage .PERIOD Deutschlands")
        ngram.get_probability("Niederlage ,COMMA Deutschlands")
        ngram.get_probability("Niederlage Deutschlands ,COMMA")
        ngram.get_probability("Niederlage Deutschlands .PERIOD")
        '''





    def parse(self):
        fp=open(self.test_file)
        for line in fp:
            string=line.split()

            for i in range(0,len(string),2):
                if i+1<len(string):
                    list=[]
                    list.append(string[i])
                    list.append(string[i+1])
                    #print "before"
                    #print list

                    stringnew=self.punctuate(list)

                    print stringnew
                    self.fw.write(stringnew+" ")

                else:
                    #print string[i]
                    self.fw.write(string[i] + " .PERIOD ")
            self.fw.write("\n")
        self.fw.close()











if __name__ == "__main__":
    clean = Clean("uncleaned_test_data.txt", "test_corpus.txt")
    ngram = NgramTest("newmodel.lm", "test_corpus.txt")


    readLM(ngram.n, "newmodel.lm")



    ngram.parse()
