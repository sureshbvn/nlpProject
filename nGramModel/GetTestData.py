
fp=open("europarl-v7.de-en.de","r")
fw=open("uncleaned_test_data.txt","w+")
i=0
for line in fp:

    i+=1

    if i<=50000:
        continue

    line = line.strip()
    fw.write(line + "\n")
    if i==55000:
        break
