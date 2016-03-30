__author__ = 'sureshbvn'


class Parsing:

    def __init__(self,fileName,nValue):
        self.file_to_be_parsed=fileName
        self.outpufile="output.txt"
        self.nValue=nValue
        self.list_of_strings=[]


    def parse(self):
        print self.file_to_be_parsed
        log = open(self.outpufile, "w")

        with open(self.file_to_be_parsed) as f:
            for line in f:
                log.write(self.pre_processing(line))

            f.close()





    def pre_processing(self,inputString):

        punctuations={',':',COMMA',':':'.PEROID','.':'.PEROID','!':'.PEROID',';':'.PERIOD','?':'?Q-MARK'}



        changed_string = ""
        for char in inputString:
            if char not in punctuations:
                changed_string = changed_string + char
            else:
                changed_string=changed_string+punctuations[char]
        return changed_string


if __name__=="__main__":
    parsing=Parsing("../trainingData/SampleFiles/input.txt",2)
    parsing.parse()

