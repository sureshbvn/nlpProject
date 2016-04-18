import properties


#POSTags = ['ADJA', 'ADJD', 'ADV', 'APPO', 'APPR', 'APPRART', 'APZR', 'ART', 'CARD', 'ITJ', 'KOKOM', 'KON', 'KOUI', 'KOUS', 'NE', 'NN', 'PDAT', 'PDS', 'PIAT', 'PIDAT', 'PIS', 'PPER', 'PPOSAT', 'PPOSS', 'PRELAT', 'PRELS', 'PRF', 'PROP', 'PTKA', 'PTKANT', 'PTKNEG', 'PTKVZ', 'PTKZU', 'PWAT', 'PWAV', 'PWS', 'STTS', 'TRUNC', 'VAFIN', 'VAIMP', 'VAINF', 'VAPP', 'VMFIN', 'VMINF', 'VMPP', 'VVFIN', 'VVIMP', 'VVINF', 'VVIZU', 'VVPP', 'XY', 'PROAV', 'FM']
ChunkTags = ['NC','VC','PC','XX']
POSTags = ['ADJA','ADJD','ADV','APPR','APPRART','APPO', 'APZR', 'ART','CARD','FM','ITJ','KOUI', 'KOUS','KON','KOKOM','NN','NE','PDS', 'PDAT', 'PIS','PIAT', 'PIDAT', 'PPER','PPOSS', 'PPOSAT', 'PRELS','PRELAT','PRF','PWS','PWAT','PWAV','PAV','PTKZU','PTKNEG','PTKVZ','PTKANT','PTKA','TRUNC','VVFIN','VVIMP','VVINF', 'VVIZU','VVPP','VAFIN', 'VAIMP','VAINF','VAPP','VMFIN','VMINF','VMPP','XY','$,','$.','$(']
class FeatureFile :

     def __init__(self,filePath):
        self.inputfile=filePath
        self.outpufile=properties.test_features_file_path
        #self.outpufile=properties.test_features_file_path
        self.fMat = []
        self.lenPOSVec = len(POSTags)
        self.lenChunkVec = len(ChunkTags)

     def featureMatrix(self):
       text_file = open(self.outpufile, "w")
       with open(self.inputfile, 'r') as inputfile:
        for line in inputfile:
            input = line.split()
            label = input[0]
            index = POSTags.index(input[2])
            index1 = ChunkTags.index(input[3])
            list_wordVec = input[4:]
            row = ''

            for i in range(self.lenPOSVec):
                if i == index:
                    row = row + str(index+1) + ':' + str(1) +" "
                else:
                    row = row + str(i+1) + ':' + str(0) +" "

            for i in range(self.lenPOSVec,self.lenPOSVec+self.lenChunkVec):
                if i == index1+self.lenPOSVec:
                    row = row + str(i+1) + ':' + str(1) +" "
                else:
                    row = row + str(i+1) + ':' + str(0) +" "

            for i in range(self.lenPOSVec+self.lenChunkVec,len(list_wordVec) + self.lenPOSVec+self.lenChunkVec):
                row = row + str(i+1) + ':' + str(list_wordVec[i-(self.lenPOSVec+self.lenChunkVec)]) +" "

            row = row + "\n"
            text_file.write(label+" "+row)
        text_file.close()

if __name__=="__main__":

   #features = FeatureFile(properties.test_tagged_output_file)
   features = FeatureFile(properties.test_tagged_output_file)
   features.featureMatrix()
