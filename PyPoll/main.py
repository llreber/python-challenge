import os
import csv

#Set data file path - different folder
#cereal_csv = os.path.join("~", "Downloads", "election_data.csv") 
#Set data file path - same folder
budget_csv = os.path.join("election_data.csv") 

with open("election_data.csv", newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    candidate = ["Khan", "Correy", "Li", "O'Tooley"]
    votecount = [0,0,0,0]
    totalCount = 0
    csv_header = next(csvreader)
    #print(csv_header)
   
    for row in csvreader:
        votename = row[2]
        totalCount = totalCount+1
        if votename  == candidate[0]:
            votecount[0] = votecount[0]+1
        if votename  == candidate[1]:
            votecount[1] = votecount[1]+1
        if votename  == candidate[2]:
            votecount[2] = votecount[2]+1
        if votename  == candidate[3]:
            votecount[3] = votecount[3]+1
        
    results = zip(candidate, votecount)
    print(candidate)
    print(votecount)
    
    output_file = os.path.join("PollOutput.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Candidate", "Votes"])

    writer.writerows(results)