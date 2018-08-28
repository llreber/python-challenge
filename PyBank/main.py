import os
import csv

#Set data file path - different folder
#cereal_csv = os.path.join("~", "Downloads", "budget_data.csv") 
#Set data file path - same folder
cereal_csv = os.path.join("budget_data.csv") 

with open("budget_data.csv", newline="", encoding="utf8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header row - you might not need the "None"
    #next(csvreader, None)
    months = 0
    cumPL = 0
     for row in csvreader:
        months = months +1
        cumPL = cumPL + float(row[1])
    
    print("Total Months: " + str(months))
    print("Cumulative P&L: "+ )str(cumPL)
        