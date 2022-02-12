# Place code below to do the analysis part of the assignment.

import csv

data = open("data/clean_data.csv", "r")
results = open("analysis_results.txt", "w")

csvreader = csv.reader(data)
next(csvreader)

sum = 0.0
firstYear = True


results.write("Anomaly averages by decade in Farenheit:\n")

for row in csvreader:
    # new decade, got sum for that decade, can calculate average and write to file
    if int(row[0])%10 == 0:
        if firstYear == True:
            firstYear = False
        else:
            results.write(str(int(row[0])-10) + "-" + str(int(row[0])-1) + ": ")
            results.write(format(sum/120, "-3f") + "\n")
            sum = 0.0
    # get 1:13 columns (J-D)
    for i in range(1, 13):
        sum += float(row[i])

data.close()
results.close()