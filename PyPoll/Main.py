import csv

file_name = "03-Python_Homework_PyPoll_Resources_election_data.csv"

with open(file_name, newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Set up a blank list that will be used to store the unique candidates
    candidates = []

    # Initializing a total_votes counter to track the total votes
    total_votes = 0
    for row in reader:
        total_votes += 1

        # As we go through the for loop, append unique candidates to the candidates list
        if row[2] not in candidates:
            candidates.append(row[2])

    # Create a dictionary to store the unique candidates as well as a place to store their total votes
    # Initiate the runningTotal variable that will be used to track each candidates total votes and assigning
    # those totals to the dictionary. Once we move on to the next candidate, we'll reset to 0

    runningTotal = 0
    CandidateVotes = { i : int(0) for i in candidates}
    for key in CandidateVotes:
        with open(file_name, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if(key == row[2]):
                    runningTotal += 1
            CandidateVotes[key] = runningTotal
            runningTotal = 0

    # Adding dictionary to track each candidate and the two values corresponding to them, total
    # votes and percent of total
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

# Used to print to terminal
print("Election Results \n-------------------------")
print(f"Total Votes: {total_votes}\n-------------------------")
for key in CandidateVotes:
    print(f"{key}: {FinalTotals[key][1]:.3f}% ({FinalTotals[key][0]})")
print(f"-------------------------\nWinner: {Winner}\n-------------------------")

# Writing to text file
f = open("Poll_Results.txt","w+")
f.write(f"Election Results \n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n")
for key in CandidateVotes:
    f.write(f"{key}: {FinalTotals[key][1]:.3f}% ({FinalTotals[key][0]})\n")
f.write(f"-------------------------\nWinner: {Winner}\n-------------------------")
# stdoutOrigin=sys.stdout
# sys.stdout = open("Poll_Results.txt","w+")