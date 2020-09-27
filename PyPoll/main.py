# import libraries
import os
import csv

# set up paths
poll_data = os.path.join("Resources","election_data_test.csv")
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
            
candidate_count = len([candidate_list])

with open(results_file, 'w') as txt_file:
    txt_file.write(f"Election Results\n ---------------------------------\n")
    txt_file.write(f"Total Votes:   {overall_vote_count}\n---------------------------------\n")
    write_index = 0
    winner_index = 0
    winner = candidate_list[0]
    for items in candidate_list:
        name = candidate_list[write_index]
        percent = votes[write_index]/overall_vote_count
        votes_for_candidate = votes[write_index]
        txt_file.write(f"{name}:  {percent}%  ({votes_for_candidate})\n")
        
        
        if votes[write_index] > votes[winner_index]:
            winner_index = write_index
            winner = candidate_list[winner_index]
       
        write_index = write_index + 1    
    txt_file.write(f"---------------------------------\n Winner: {winner}\n---------------------------------\n")


           
           
           




# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

