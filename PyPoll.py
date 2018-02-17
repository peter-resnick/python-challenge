import os 
import csv

csvpath = os.path.join("..","..","PyPoll","raw_data","election_data_1.csv")
k = 0

print("Election Results")
print("----------------------")

with open(csvpath, newline="") as csvfile:
    dataSet = csv.reader(csvfile, delimiter=",")

    total_votes = 0
    for row in dataSet:
        total_votes = total_votes + 1
    print("Total Votes: " + str(total_votes - 1))

    print("------------------------")

with open(csvpath, newline="") as csvfile:
    dataSet = csv.reader(csvfile, delimiter=",")

    candidates = []
    for rows in dataSet:
        current_row = row
        next_row = next(dataSet)
        if current_row != next_row:
            candidates.append(next_row)

    print(candidates[])