# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
# set path for csv file as 
budget_data = os.path.join( "Resources", "budget_data.csv")
#set up path for saving output to text file
output_data = os.path.join("Analysis","Financial_Analysis.txt")


# read the Csv file and set up a loop to count rows
with open(budget_data, 'r') as csv_file:
    csv_monthly = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    #Initialize Variables
    Months = 0
    TotalProfit = 0
    RevChange = 0
    PrevRev = 0

    #Set up Lists
    ProfitChangeList = []
    GreatestGain = ["",0] 
    GreatestLoss = ["",0]
    

    for rows in csv_monthly:
        # Count months and derive total profit
        Months = Months + 1
        TotalProfit = TotalProfit + int(rows[1])
        
        #Calculate  revenue change for the month    
        RevChange = int(rows[1]) - PrevRev
        PrevRev = int(rows[1])    
        
        #Save the revenue change into a list
        if Months > 1:
            ProfitChangeList.append(RevChange)
        
        #Compare the current month revenue to the previous GreatestGain & save the month and $change if greater
        if (RevChange > GreatestGain[1]):
            GreatestGain[0]=rows[0]
            GreatestGain[1]=RevChange

        #Compare the current month revenue to the previous GreatestLoss & save ithe month and $change if lower
        if (RevChange < GreatestLoss[1]):
            GreatestLoss[0]=rows[0]
            GreatestLoss[1]=RevChange

# Calculate total of all monthly changes in proit/loss and compute the average change as well
sumMonChg =sum(ProfitChangeList)
print(f'sum of monthly change {sumMonChg}')
avgMonChg = round(sum(ProfitChangeList)/len(ProfitChangeList),2)


# Print output to terminal
print("Financial Analysis \n--------------------------------")
print(f"Total Months:  {Months}\n" f"Total Revenue:   ${TotalProfit}")
print(f'Average Change: ${avgMonChg}')
print(f'Greatest Increase in Profits: {GreatestGain[0]} (${GreatestGain[1]})')
print(f'Greatest Decrease in Profits: {GreatestLoss[0]} (${GreatestLoss[1]})')

#Write data to the txt file
with open(output_data, 'w') as txt_file:
    txt_file.write("Financial Analysis \n--------------------------------\n")
    txt_file.write(f"Total Months:    {Months}\n")
    txt_file.write(f"Total Revenue:   ${TotalProfit}\n")
    txt_file.write(f'Average Change: ${avgMonChg}\n')
    txt_file.write(f'Greatest Increase in Profits: {GreatestGain[0]} (${GreatestGain[1]})\n')
    txt_file.write(f'Greatest Decrease in Profits: {GreatestLoss[0]} (${GreatestLoss[1]})\n')


