import os
import csv

#Set data file path - same folder
bank_csv = os.path.join("budget_data.csv") 

with open("budget_data.csv", newline="", encoding="utf8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header row - you might not need the "None"
    next(csvreader, None)

    #initialize the variables
    months = 0
    cumPL = 0
    FirstMoPL = 0
    LastMoPL = 0
    PrevMoPL = 0
    GreatIncrease = 0
    GreatDecrease = 0
    #Read the monthly date by row
    for row in csvreader:
        months = months +1
        CurrMoPL = float(row[1])
        #calculate the cumulative P&L
        cumPL = cumPL + CurrMoPL
        #Find the difference between this month and the last month
        MonthDiff = CurrMoPL - PrevMoPL
        #check for the max monthly increase and max monthly drcrease
        if MonthDiff > GreatIncrease:
            GreatIncrease = MonthDiff
            IncreaseMonth = row[0]
        if MonthDiff < GreatDecrease:
            GreatDecrease = MonthDiff
            DecreaseMonth = row[0]
        if months == 1:
            FirstMoPL = float(row[1])
        LastMoPL = CurrMoPL
        PrevMoPL = CurrMoPL
    
    #output the results to the screen
    print("Financial Analysis")
    print("Total Months: " + str(months))
    print("Cumulative P&L: "+ str(cumPL))
    AvePLChange = round((LastMoPL - FirstMoPL)/(months -1),2)
    print("Average monthly change: " + str(AvePLChange))
    print("Greatest monthly increase: " + IncreaseMonth +" "+ str(GreatIncrease))
    print("Greatest monthly decrease: " + DecreaseMonth +" "+ str(GreatDecrease))

    results = [months, cumPL, AvePLChange, IncreaseMonth, GreatIncrease, DecreaseMonth, GreatDecrease]
    headings = ["Number of Months", "Cumulative P&L", "Average Monthly Change", "Month of Greatest Increase","Greatest Monthly Increase", "Month of Greatest Decrease","Greatest Monthly Decrease"]
    combined = zip(headings, results)

    output_file = os.path.join("PyBankOutput.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])

    writer.writerows(combined)