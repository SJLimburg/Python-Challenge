# Python-Challenge

Challenge 1 - PyBank

This challenge has two parts. The first challenge is to analyze financial;s records from a fictious  company. The second challenge is to help a small rural town modernize its voting system.

This challenge illusrates how to read a csv file that contains sequential monthly dates and a Profit/Loss entry as input. That data is used to output the following results to a .txt file:

1. The total number of months included in the dataset 

        The skill practiced is simply creating and incrementing a variable in a FOR LOOP. Each row in the file represents a month under report.

2.  The net total amount of "Profit/Losses" over the entire period

        The solution also used a FOR LOOP to add each month profit/loss to the running total. Within th eFOR LOOP a LIST INDEX was required to indicate which column of data was to be added each iteration

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

Challenge 2 - PyPoll

This challenge is to automate processing of polling data for a ficticious municipality.

The data provide is a .csv file with Voter ID, County and Candidate.  The script will only work when the data is in this particular csv format.

TThis challenge illusrates how to read a csv file that contains fictitious polling data for over 3 million votes. Using excel would not easily work due to more than 3 million votes. 
That fictitios data was used  to output the following results to a .txt file:

1.      The total number of votes cast

                While the file was read a loop iterated to tally the total votes.

2.      A complete list of candidates who received votes

                An empty List was created; A loop was created to append the List with each candidates name every time a new name was found in the data. Using indexes the vote count for each of the candidates was tallied withion the same loop.

3.      The percentage of votes each candidate won

                Arithmetic operators were used to calculate the percentage. Candidate total *100 / total votes was sent to both the terminal and to a .txt file for each of the candidates

4.      The total number of votes each candidate won

                Individual totals by candidate was retrieved from the List using indexes. It also became part of the percentage calculation.

5.      The winner of the election based on popular vote.

                A loop with a coparison was set up to determine the winner.

The 5 outputs were printed to the screen as well as written to an output file.

