__author__ = 'sureshbvn'
import  nltk
from nltk.util import ngrams
from nltk.probability import ConditionalProbDist




class Parsing:
    def __init__(self, fileName, nValue):
        self.file_to_be_parsed = fileName
        self.outpufile = "output.txt"
        self.outpufile_modified="ouput_modified.txt"
        self.nValue = nValue
        self.list_of_strings = []





    def calculate_probablities(self):
        fp=open("output.txt")
        for line in fp:
            print line

    def parse(self):
        print self.file_to_be_parsed
        log = open(self.outpufile, "w")






        with open(self.file_to_be_parsed) as f:
            for line in f:

                log.write(self.pre_processing(line)+"\n")

            f.close()

    def pre_processing(self, inputString):

        punctuations = {',': ' ,COMMA ', ':': ' .PEROID ', '.': ' .PERI0D ', '!': ' .PEROID ', ';': ' .PERIOD ', '?': ' ?Q-MARK ',' ':' epsilon '}

        changed_string = ""
        for char in inputString:
            if char not in punctuations:
                changed_string = changed_string + char
            else:
                changed_string = changed_string + punctuations[char]
        return changed_string

    def modified_pre_processing(self, inputString):
        punctuations = {',COMMA  epsilon':',COMMA','.PERIOD epsilon':'.PERIOD'}
        print "inside"

        changed_string = ""
        for char in inputString:
            if char not in punctuations:
                changed_string = changed_string + char
            else:
                changed_string = changed_string + punctuations[char]
                print "yes"
        return changed_string
    def parse_modified(self):
        print self.file_to_be_parsed
        log = open(self.outpufile_modified, "w")






        with open(self.outpufile) as f:
            for line in f:

                line = line.replace(',COMMA  epsilon', ',COMMA')
                line = line.replace('.PERIOD epsilon','.PERIOD')

                log.write(line)

            f.close()
    def create_vocabular(self,vocab_file):
        punctuations = {',': ' ,COMMA ', ':': ' .PEROID ', '.': ' .PERI0D ', '!': ' .PEROID ', ';': ' .PERIOD ',
                        '?': ' ?Q-MARK ', ' ': ' epsilon '}

        voc=open(vocab_file,"w+")

        train=open(self.file_to_be_parsed,"r")
        for line in train:
            words=line.split()
            for word in words:
                if word not in punctuations.keys():
                    word=word.replace(",","")
                    word = word.replace(".", "")
                    voc.write(word+"\n")
        voc.close()
        train.close()


if __name__ == "__main__":



    parsing = Parsing("file1.txt", 4)
    parsing.create_vocabular("vocab.txt")
    parsing.parse()
    parsing.calculate_probablities()
    parsing.parse_modified()
