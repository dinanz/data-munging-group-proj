# Place code below to do the munging part of this assignment.

raw = open("data/raw_data.txt", "r")

clean = open("clean_data.csv", "w")

gotHeaders = False

# loop through lines in raw text
for line in raw:
    curLine = line.rstrip().split()
    if len(curLine) != 0:

        # get headers
        if curLine[0] == "Year" and gotHeaders == False:
            for i in range(0, len(curLine)-2):
                clean.write(curLine[i])
                clean.write(",")
            clean.write(curLine[-2])
            clean.write("\n")
            gotHeaders = True

        # if line of data
        if curLine[0].isnumeric():
            clean.write(curLine[0])
            clean.write(",")
            for i in range(1, len(curLine)-2):
                if curLine[i][0] != "*":
                    num = float(curLine[i])
                    clean.write(format(num/100*1.8, ".1f"))
                else:
                    # for missing values, subsitute 0 for now
                    clean.write("0")
                clean.write(",")
            if curLine[-2][0] != "*":
                num = float(curLine[-2])
                clean.write(format(num/100*1.8, ".1f"))

            clean.write("\n")


clean.close()
raw.close()