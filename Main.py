import csv

file_name = "03-Python_Homework_PyBank_Resources_budget_data.csv"

with open(file_name, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    # row represents each row in the csv file
    # the type of the row object is a list
    Months = 0
    NetAmt = 0
    PrevPL = 0
    Delta = 0
    PLTot = []
    # This will skip the first row of the csv file
    next(csvreader)
    for row in csvreader:
        if row == 1:
            PL = int(row[1])
            Months += 1
            NetAmt = NetAmt + PL
            PrevPL = PL
        else:
            PL = int(row[1])
            Delta = Delta + (PL - PrevPL)
            Months += 1
            NetAmt = NetAmt + PL
            PrevPL = PL
    AvgDelta = Delta / Months

output_file = "Resources_Budget_output.csv"
with open(output_file, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Months: ", Months])
    csvwriter.writerow(["Total: ", NetAmt])
    csvwriter.writerow(["Average Change: ", AvgDelta])
    csvwriter.writerow(["Total: ", Delta])