__author__ = 'sureshbvn'
import  nltk
from nltk.util import ngrams
from nltk.probability import ConditionalProbDist




class Parsing:
    def __init__(self, fileName, nValue):
        self.file_to_be_parsed = fileName
        self.outpufile = "output.txt"
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

        punctuations = {',': ' ,COMMA', ':': ' .PEROID', '.': ' .PEROID', '!': ' .PEROID', ';': ' .PERIOD', '?': ' ?Q-MARK'}

        changed_string = ""
        for char in inputString:
            if char not in punctuations:
                changed_string = changed_string + char
            else:
                changed_string = changed_string + punctuations[char]
        return changed_string


if __name__ == "__main__":
    parsing = Parsing("input.txt", 3)
    parsing.parse()
    parsing.calculate_probablities()
