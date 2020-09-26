# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
# set path for csv file as 
budget_data = os.path.join( "Resources", "budget_data.csv")
# C:\Users\Shirley\Desktop\Homework_BC_SJL\03-Homeworrk_Python\Python-Challenge\PyBank


# read the Csv file and set up a loop to count rows
with open(budget_data, 'r') as csv_file:
    csv_monthly = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    print(f"Header: {csv_header}")

    Months = 0
    TotalProfit = 0
    AvgMonChange = 0

    for rows in csv_monthly:
        TotalProfit = TotalProfit  + int(rows[1])
       


#  Inside loop have a Variable Months to increment every loop to derive total months under report.
# Also loop through
#  MonthlyChange =  (curMonPL - prevMonPl ) to get difference ;
#  TotalProfit = TotalProfit  + Col2
#  TotalMonthyChange =  TotalMonthyChange + MonthlyChange:
# Average Monthly Change = TotalMonthyChange/Months
# conditional loop:
# Set GreatestGain to  first MonthlyChange, Store amount and month - go to next and compare
# set GreatestLoss to the first MonthlyChange   Store amount and month - go to next and compare  - Beware of subtraction differences.   

# The total number of months included in the dataset - file name budget_data.csv
# The net total amount of "Profit/Losses" over the entire period - Get the sum of all months p/l
# The average of the changes in "Profit/Losses" over the entire period - get the mean of p/l
# The greatest increase in profits (date and amount) over the entire period - MOM calculation Mon2-mon1 etc = monthly change
# The greatest decrease in losses (date and amount) over the entire period - MOM calculation - greatest MOM negative
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Total months
# total net profit/loss
print(TotalProfit)
# average monthyly change in profit
# greatest monthly increase amount and month
# greatest monthly decrease amount and month

# # Import necessary dependencies
# import csv
# # Create the path for the filename
# data_output = os.path.join("Analysis", "PyBank.txt")
# # Write data to a .csv file
# with open(data_output, "w", newline="") as csvfile:
#  writer = csv.writer(csvfile)
#  # To save specific data input as a row in the csv
#  writer.writerow(["row1", "row2"])

