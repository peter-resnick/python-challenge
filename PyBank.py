import os 
import csv

csvpath = os.path.join("..","..","PyBank","raw_data","budget_data_1.csv")
k = 0
with open(csvpath, newline="") as csvfile:
    dataSet = csv.reader(csvfile, delimiter=",")

   num_months = 0
    for row in dataSet:
        num_months = num_months + 1
    print("Total Months: " + str(num_months - 1))

with open(csvpath, newline="") as csvfile:
    dataSet = csv.reader(csvfile, delimiter=",")
    for rows in dataSet:
        k = k + int(row[1])

   print("Total Revenue: $" + str(k))

   avg_change = k/num_months
    print("Average Revenue Change: $" + str(round(avg_change,2)))

max_rev = 0
max_date = 0

with open(csvpath, newline="") as csvfile:
    dataSet = csv.reader(csvfile, delimiter=",")
    next(dataSet)
    
   for rows in dataSet:
        if int(row[1]) > int(max_rev):
            max_rev = int(row[1])
            max_date = row[0]

   print("Greatest Increase in Revenue: " + str(max_date) + " ($" + str(max_rev) + ")")

with open(csvpath, newline="") as csvfile:
    dataSet = csv.reader(csvfile, delimiter=",")
    min_rev = 10000000000
    min_date = 0
    for rows in dataSet:
        if int(row[1]) < int(min_rev):
            min_rev = row[1]
            min_date = row[0]

   print("Greatest Decrease in Revenue: " + str(min_date) + " ($" + str(min_rev) + ")")