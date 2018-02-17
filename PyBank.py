import os 
import csv

csvpath = os.path.join("..","NUCHI201801DATA4-Class-Repository-Data","MWS","Homework","03-Python","Instructions","PyBank","budget_data_1.csv")

with open(csvpath, newline="") as csvfile:
    dataset = csv.reader(csvfile, delimiter=",")

num_months = sum(1 for row in dataset)
print("Total Months: " + str(num_months))

for rows in dataset:
    k = k + row[1]

print("Total Revenue: $" + str(k))

avg_change = k/num_months
print("Average Revenue Change: $" + str(avg_change))

#for rows in csvreader:
 #  'if row[0] == row.next()[0]
  #      k = k + 1