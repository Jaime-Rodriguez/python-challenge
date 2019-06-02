import csv

file_name = "03-Python_Homework_PyPoll_Resources_election_data.csv"
total_votes = 0
candidates = []
with open(file_name, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        total_votes += 1
for row in csvreader:
    if row[2] not in candidates:
        candidates.append(row[2])

#     Months = 0
#     NetAmt = 0
#     PLCurr = 0
#     PLPrev = 0
#     Delta = 0
#     Count = 0
#     GreatInc = 0
#     GreatIncMonth = ""
#     GreatDec = 0
#     GreatDecMonth = ""
#
#     # This will skip the first row of the csv file
#     next(csvreader)
#     for row in csvreader:
#         if Count == 0:
#             PLCurr = int(row[1])
#             Months += 1
#             NetAmt = NetAmt + PLCurr
#             PLPrev = PLCurr
#             Count = 1
#         else:
#             PLCurr = int(row[1])
#             Delta = Delta + (PLCurr - PLPrev)
#             # Compare the delta with what is stored in our greatest increase/decrease variables
#             if (GreatInc < PLCurr - PLPrev):
#                 GreatInc = PLCurr - PLPrev
#                 GreatIncMonth = row[0]
#             if (GreatDec > PLCurr - PLPrev):
#                 GreatDec = PLCurr - PLPrev
#                 GreatDecMonth = row[0]
#             Months += 1
#             NetAmt = NetAmt + PLCurr
#             PLPrev = PLCurr
#             Count += 1
#
#     AvgDelta = Delta / (Count - 1)
#
#
# print("Financial Analysis\n ------------------------")
# print(f"Total Months: {Months}\nTotal: ${NetAmt}\nAverage Change: ${AvgDelta:.2f}\nGreatest Increase"
#       f"in Profits: {GreatIncMonth} (${GreatInc})\nGreatest Decrease in Profits: {GreatDecMonth} (${GreatDec})")
#
#
# # Write a file that will export the print statements from above to a text file named "budget_data.txt"
# f = open("budget_data.txt","w+")
# f.write(f"Financial Analysis\n ------------------------\nTotal Months: {Months}\nTotal: ${NetAmt}\nAverage Change: ${AvgDelta:.2f}\nGreatest Increase in Profits: {GreatIncMonth} (${GreatInc})\nGreatest Decrease in Profits: {GreatDecMonth} (${GreatDec})")
#
