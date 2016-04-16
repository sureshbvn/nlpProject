



fp=open("europarl-v7.de-en.de","r")
fw=open("TrainingCorpus3.txt","w+")
i=0
for line in fp:
    line=line.strip()
    fw.write(line+"\n")
    i+=1

    if i==1000000:
        break