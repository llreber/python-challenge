import os
import csv

#Set data file path - different folder
#cereal_csv = os.path.join("~", "Downloads", "election_data.csv") 
#Set data file path - same folder
budget_csv = os.path.join("election_data.csv") 

with open("election_data.csv", newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # initialize variables
    candidate = []
    candidateCount = 0
    #candidate = ["Khan", "Correy", "Li", "O'Tooley"]
    votecount = [0, 0, 0, 0]
    votePct = [0, 0, 0, 0]
    totalCount = 0
    csv_header = next(csvreader)
    #print(csv_header)
   
    for row in csvreader:
        totalCount = totalCount+1
        #check for unique candidate names and append to list
        if row[2] not in candidate:
            candidate.append(row[2])
            candidateCount = candidateCount + 1
        #check the candidate woted for and increment the vote count
        for x in range(candidateCount):
            if row[2] == candidate[x]:
                votecount[x] = votecount[x] + 1

    #calculate the percent of votes received
    for x in range(candidateCount):
        votePct[x] = round(100*votecount[x]/totalCount, 2)

    #create the results tuple                
    results = zip(candidate, votecount, votePct)

    #find the winner
    winner = votecount.index(max(votecount))
    
    #output the results to the screen
    print("Election Results")
    print("Total Votes: " + str(totalCount))
    for x in range(candidateCount):
        print(candidate[x] + " " +str(votePct[x]) + "% (" +str(votecount[x]) + ")")
   
    print("Winner: " + candidate[winner])
   
    output_file = os.path.join("PollOutput.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])
    writer.writerow(["Winner: ", candidate[winner]])
    writer.writerow(["Total votes cast: ", totalCount])
    writer.writerow(["Candidate", "Votes", "Percet of Votes"])
    writer.writerows(results)