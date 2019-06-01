import csv

file_name = "03-Python_Homework_PyBank_Resources_budget_data.csv"

with open(file_name, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
# Initiate the variables for counting the total months, the net PL amount, the previous PL amount
# the delta from current and previous PL number
    Months = 0
    NetAmt = 0
    PLCurr = 0
    PLPrev = 0
    Delta = 0
    PLTot = []
    Count = 0
    GreatInc = 0
    GreatIncMonth = ""
    GreatDec = 0
    GreatDecMonth = ""

    # This will skip the first row of the csv file
    next(csvreader)
    for row in csvreader:
        if Count == 0:
            PLCurr = int(row[1])
            Months += 1
            NetAmt = NetAmt + PLCurr
            PLPrev = PLCurr
            Count = 1
        else:
            PLCurr = int(row[1])
            Delta = Delta + (PLCurr - PLPrev)
            # Compare the delta with what is stored in our greatest increase/decrease variables
            if (GreatInc < PLCurr - PLPrev):
                GreatInc = PLCurr - PLPrev
                GreatIncMonth = row[0]
            if (GreatDec > PLCurr - PLPrev):
                GreatDec = PLCurr - PLPrev
                GreatDecMonth = row[0]
            Months += 1
            NetAmt = NetAmt + PLCurr
            PLPrev = PLCurr
            Count += 1

    AvgDelta = Delta / (Count - 1)


print("Financial Analysis\n ------------------------")
print(f"Total Months: {Months}\nTotal: ${NetAmt}\nAverage Change: ${AvgDelta:.2f}\nGreatest Increase"
      f"in Profits: {GreatIncMonth} (${GreatInc})\nGreatest Decrease in Profits: {GreatDecMonth} (${GreatDec})")

cat > "budget_data.txt"

output_file = "Resources_Budget_output.csv"
with open(output_file, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Months:", Months])
    csvwriter.writerow(["Total:", '${:,.2f}'.format(NetAmt)])
    csvwriter.writerow(["Average Change:", AvgDelta])
    csvwriter.writerow(["Greatest Increase in Profits:", GreatIncMonth,GreatInc])
    csvwriter.writerow(["Greatest Decrease in Profits:", GreatDecMonth,GreatDec])
    csvwriter.writerow(["Count:", Count])