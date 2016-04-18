
fp=open("finalmodel.lm","r")
fw=open("newmodel.lm","w+")
for line in fp:
    str=line.strip()
    nextstring=""



    if str=="\\1-grams:":
        fw.write(str+"\n")
        for line in fp:
            str1 = line.strip()
            if str1=="\\2-grams:":
                nextstring="\\2-grams:"

                break
            words=line.split()
            if len(words)>0:
                print words[0]
                words[0]=-3+float(words[0])

                words[0] = "%.9f" % words[0]
                print words[0]
                stringOutput = '\t'.join(words)

                fw.write(stringOutput+"\n")
    if nextstring == "\\2-grams:":
        fw.write(nextstring+"\n")
        for line in fp:
            str1 = line.strip()
            if str1 == "\\3-grams:":
                nextstring = "\\2-grams:"

                break
            words = line.split()
            if len(words) > 0:
                print words[0]
                words[0] = -2 + float(words[0])

                words[0] = "%.9f" % words[0]
                print words[0]
                stringOutput = '\t'.join(words)

                fw.write(stringOutput + "\n")
    if nextstring == "\\3-grams:":
        fw.write(nextstring+"\n")
        for line in fp:
            str1 = line.strip()
            if str1 == "\\4-grams:":
                break
            words = line.split()
            if len(words) > 0:
                print words[0]
                words[0] = -2 + float(words[0])
                words[0] = "%.9f" % words[0]
                print words[0]
                stringOutput = '\t'.join(words)
                fw.write(stringOutput + "\n")

    fw.write(line)
fw.close()





