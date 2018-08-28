import os
import csv

#Set data file path - different folder
#cereal_csv = os.path.join("~", "Downloads", "budget_data.csv") 
#Set data file path - same folder
budget_csv = os.path.join("budget_data.csv") 

with open("budget_data.csv", newline="", encoding="utf8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")