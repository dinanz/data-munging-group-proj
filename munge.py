# Place code below to do the munging part of this assignment.

raw = open("data/raw_data.txt", "r")

clean = open("clean_data.csv", "w")

gotHeaders = False

for line in raw:
    curLine = line.rstrip().split()
    if len(curLine) != 0:
        if curLine[0] == "Year" and gotHeaders == False:
            for i in range(0, len(curLine)-2):
                clean.write(curLine[i])
                clean.write(",")
            clean.write(curLine[-2])
            clean.write("\n")
            gotHeaders = True
        if curLine[0].isnumeric():
            clean.write(curLine[0])
            clean.write(",")
            for i in range(1, len(curLine)-2):
                #print(curLine[i])
                if curLine[i].isnumeric() or (curLine[i][0] == "-" and curLine[i][1:].isnumeric()):
                    num = float(curLine[i])
                    num = (num/100*1.8)
                    num = format(num, ".1f")
                    clean.write(num)
                else:
                    clean.write(curLine[i])
                clean.write(",")
            if curLine[-2][0] != "*":
                num = float(curLine[-2])
                num = (num/100*1.8)
                num = format(num, ".1f")
                clean.write(num)
            clean.write("\n")


clean.close()
raw.close()