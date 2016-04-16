import itertools
from srilm import *


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
        print combination_list

    def get_probability(self, ngram):

        length = self.length_of_sentence(ngram)


        if length>5:
            raise ValueError('The n value specified is greater than 5')
        p6 = getNgramProb(self.n, ngram,length)
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

        print string_list

        string1=str(string_list[0]+" "+",COMMA"+" "+string_list[1]+" .PERIOD")

        print "The string 1 is " +string1
        '''
        string12 = str(string_list[0].title() + " " + ",COMMA" + " " + string_list[1] + " .PERIOD")
        string13 = str(string_list[0] + " " + ",COMMA" + " " + string_list[1],title()+ " .PERIOD")


        string14 = str(string_list[0].title() + " " + ",COMMA" + " " + string_list[1].title() + " .PERIOD")
        '''

        string2 = str(string_list[0] + " " + ".PERIOD" + " " + string_list[1] + " ,COMMA")
        '''
        string22 = str(string_list[0].title() + " " + ".PERIOD" + " " + string_list[1] + " ,COMMA")
        string23 = str(string_list[0] + " " + ".PERIOD" + " " + string_list[1].title() + " ,COMMA")
        string24 = str(string_list[0].title() + " " + ".PERIOD" + " " + string_list[1].title() + " ,COMMA")
        '''


        string3 = str(string_list[0] + " " + " " + string_list[1] + " .PERIOD")
        '''
        string32 = str(string_list[0].title() + " " + " " + string_list[1] + " .PERIOD")
        string33 = str(string_list[0] + " " + " " + string_list[1].title() + " .PERIOD")
        string34 = str(string_list[0].title() + " " + " " + string_list[1].title() + " .PERIOD")
        '''

        string4 = str(string_list[0] + " " + ",COMMA" + " " + string_list[1])
        string5 = str(string_list[0] + " " + " " + string_list[1] + " ,COMMA")
        string6 = str(string_list[0] + " " + ".PERIOD" + " " + string_list[1])
        string7 = str(string_list[0] + " " + string_list[1])




        prob1=ngram.get_probability(string1)
        print prob1
        prob2 = ngram.get_probability(string2)
        prob3 = ngram.get_probability(string3)
        prob4 = ngram.get_probability(string4)
        prob5 = ngram.get_probability(string5)
        prob6 = ngram.get_probability(string6)
        prob7 = ngram.get_probability(string7)

        prob_list={}
        prob_list[float(prob1)]=string1
        prob_list[float(prob2)] = string2
        prob_list[float(prob3)] = string3
        prob_list[float(prob4)] = string4
        prob_list[float(prob5)] = string5
        prob_list[float(prob6)] = string6
        prob_list[float(prob7)] = string7
        #print prob_list

        maxValue=self.max_in_list(prob_list)
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
                    print "before"
                    print list

                    stringnew=self.punctuate(list)
                    print stringnew
                    self.fw.write(stringnew+" ")

                else:
                    print string[i]
                    self.fw.write(string[i] + ".PERIOD")
            self.fw.write("\n")
        self.fw.close()











if __name__ == "__main__":
    ngram = NgramTest("final_corpus.lm", "test_output.txt")

    readLM(ngram.n, "final_corpus.lm")



    ngram.parse()
