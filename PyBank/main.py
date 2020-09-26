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


    

# The total number of months included in the dataset - file name budget_data.csv


# The net total amount of "Profit/Losses" over the entire period - Get the sum of all months p/l


# The average of the changes in "Profit/Losses" over the entire period - get the mean of p/l


# The greatest increase in profits (date and amount) over the entire period - MOM calculation Mon2-mon1 etc = monthly change


# The greatest decrease in losses (date and amount) over the entire period - MOM calculation - greatest MOM negative

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#Totak months
# total net profit/loss
# average monthyly profit
# greatest monthly increase amount and month
# greatest monthly decrease amount and month


