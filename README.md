# Python-Challenge

This challenge has two parts. The first challenge is to analyze financial;s records from a fictious  company. The second challenge is to help a small rural town modernize its voting system.

This challenge illusrates how to read a csv file that contains sequential monthly dates and a Profit/Loss entry as input. That data is used to output the following results to a .txt file:

1. The total number of months included in the dataset 

        The skill practiced is simply incrementing a v ariable in the for loop

2.  The net total amount of "Profit/Losses" over the entire period

        The solution also used a for loop to add each month profit within the loop. A list index was required to indicate which column of data was added each iteration

3.  The average of the changes in "Profit/Losses" over the entire period

        The changes in Profit/Losses by month was solved by by subtracting the previous month Profit/Loss value from the current month entry. 
        To avoid subtracting a null or -0 value an if statement ensured the calculation began at the second month of the report.
        The results for each month were stored in a list. The sum of the list values and the count of the list items was used to derive the average monthly change

4. The greatest increase in profits (date and amount) over the entire period

        A list type variable was used to store the first monthly change value and date associated with it 
        Each iteration compared the current value to the stored loop variable.
        If the current month value was greater than the stored value,  the list variable was updated

The greatest decrease in losses (date and amount) over the entire period

        A list type variable was used to store the first monthly change value and date associated with it 
        Each iteration compared the current value to the stored loop variable.
        If the current month value was lower than the stored value,  the list variable was updated

The results of the previous calculations were printed to the terminal and also printed to a .txt file which was stored in the Analysis folder

The second challenge is to help a small rural town modernize its voting system. 

