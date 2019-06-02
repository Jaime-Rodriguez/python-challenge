import csv

#
file_name = "03-Python_Homework_PyPoll_Resources_election_data.csv"
total_votes = 0

with open(file_name, newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    candidates = []
    for row in reader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])

    # Add the candidates to a dictionary so that we can set calculate the
    CandidateVotes = { i : int(0) for i in candidates}

    runningTotal = 0
    for key in CandidateVotes:
        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if(key == row[2]):
                    runningTotal += 1
            CandidateVotes[key] = runningTotal
            runningTotal = 0

    print(CandidateVotes)
    FinalTotals = {}
    for key in CandidateVotes:
        # FinalTotals.append(key)
        # FinalTotals.append(CandidateVotes[key])
        # FinalTotals.append(CandidateVotes[key]/total_votes)
        FinalTotals[key] = (CandidateVotes[key],(CandidateVotes[key]/total_votes)*100)
    # Use this counter to determine who had the most votes
    WinningCounter = 0
    Winner = ""
    for key in CandidateVotes:
        if CandidateVotes[key] > WinningCounter:
            Winner = key
            WinningCounter = CandidateVotes[key]
        # CandidateVotes[key].append(CandidateVotes[key] / total_votes)


print("Election Results \n-------------------------")
print(f"Total Votes: {total_votes}\n-------------------------")
for key in CandidateVotes:
    print(f"{key}: {FinalTotals[key][1]:.3f}% ({FinalTotals[key][0]})")
print(f"-------------------------\nWinner: {Winner}\n-------------------------")

f = open("Poll_Results.txt","w+")
f.write(f"Election Results \n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n")
for key in CandidateVotes:
    f.write(f"{key}: {FinalTotals[key][1]:.3f}% ({FinalTotals[key][0]})\n")
f.write(f"-------------------------\nWinner: {Winner}\n-------------------------")
# stdoutOrigin=sys.stdout
# sys.stdout = open("Poll_Results.txt","w+")