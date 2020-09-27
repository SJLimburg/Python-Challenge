# import libraries
import os
import csv

# set up paths
poll_data = os.path.join("Resources","election_data.csv")
results_file = os.path.join("Analysis","Election_Results.txt")

# read csv file
with open(poll_data, 'r') as vote_file:
    csv_votes = csv.reader(vote_file, delimiter=",")
    csv_header = next(vote_file)
 
# set up variables
    overall_vote_count = 0

# set up lists
    candidate_list = []
    votes = []

# loop to count votes per candidate 
    for row in csv_votes:
        #Total vote counter
        overall_vote_count = overall_vote_count + 1

        #Who received the vote for this row
        candidate_name = row[2]
    
        #Increent voet for candidate in the list or add a new candidate name to candidate list + 1 vote
        if candidate_name in candidate_list:
            candidate_index = candidate_list.index(candidate_name)
            votes[candidate_index] = votes[candidate_index] + 1
        else:
            candidate_list.append(candidate_name)
            votes.append(1)
            temp = len([votes])

           
           
           




# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

