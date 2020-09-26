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

    Months = 0
    TotalProfit = 0
    RevChange = 0
    ProfitChangeList = []
    PrevRev = 0
    GreatestGain = ["",0] 
    GreatestLoss = ["", -100]
    

    for rows in csv_monthly:
        # Count months and derive total profit
        Months = Months+1
        TotalProfit = TotalProfit  + int(rows[1])
        #Calculate  revenue change for the month
        RevChange = int(rows[1]) - PrevRev
        PrevRev = int(rows[1])
        #Save the revenue change into a list
        ProfitChangeList.append(RevChange)
        
        #Compare the current month revenue to the previous GreatestGain & save if greater
        if (RevChange > GreatestGain[1]):
            GreatestGain[0]=rows[0]
            GreatestGain[1]=RevChange

        #Compare the current month revenue to the previous GreatestLoss & save if worse
        if (RevChange < GreatestLoss[1]):
            GreatestLoss[0]=rows[0]
            GreatestLoss[1]=RevChange

# print(*ProfitChangeList, sep =", ")
# avgMonChg = sum(ProfitChangeList)/len(ProfitChangeList)
# print(avgMonChg)

# checking output for eventual writing into output file
print("Financial Analysis \n--------------------------------\n")
print(f"Total Months:  {Months}\n" f"Total Revenue:   ${TotalProfit}\n")
print(f'Greatest Increase in Profits: {GreatestGain[0]} (${GreatestGain[1]})')
print(f'Greatest Decrease in Profits: {GreatestLoss[0]} (${GreatestLoss[1]})')



# with open(data_output, "w", newline="") as txt_file:
#  writer = txt.writer(txt_file)
#  # To save specific data input as a row in the csv
#  writer.writerow(["row1", "row2"])

