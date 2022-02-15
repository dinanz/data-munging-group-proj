# Raw Data Munging

## Group members
Jovi Koh (jlk668) <br>
John <br>
Diana Zhao (dz1371)

## Munging
The cleaning of the raw data is fairly simple: the program takes in the raw data file, and goes through each row to store or not store them. The program will stor the first header, and ignores all subsequent headers. For each row that starts with a year, the program will split the row by spaces, and  read and store all data points into floats, then write it to the clean output csv file.

## Analysis
This is also a simple program: reading the 120 data points for each month every decade and calculating the average of those 120 data points will yield the most accurate results. The program will, for each decade, read and calculate the sum of those 120 data points, then divide it by 120 to get the average temperature fluctuation within the decade, and then print those averages to an output text file.

## Input/output files
Raw data: [data/raw_data.txt](https://github.com/dinanz/data-munging-group-proj/blob/master/data/raw_data.txt)<br>
Cleaned up data in csv: [data/clean_data.csv](https://github.com/dinanz/data-munging-group-proj/blob/master/data/clean_data.csv)<br>
Analysis results in text file: [analysis_results.txt](https://github.com/dinanz/data-munging-group-proj/blob/master/analysis_results.txt)
