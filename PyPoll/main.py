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
    
        #Increment voet for candidate in the list or add a new candidate name to candidate list + 1 vote
        if candidate_name in candidate_list:
            candidate_index = candidate_list.index(candidate_name)
            votes[candidate_index] = votes[candidate_index] + 1
        else:
            candidate_list.append(candidate_name)
            votes.append(1)  
            

#Begin populating output file
with open(results_file, 'w') as txt_file:

    #Output banner and Total Votes data to output file
    txt_file.write(f"Election Results\n------------------------\n")
    txt_file.write(f"Total Votes:   {overall_vote_count}\n-------------------------\n")

    # Print the same to the terminal screen
    print(f"Election Results\n ------------------------")
    print(f"Total Votes:   {overall_vote_count}\n-------------------------")

    # Set up variables for loop to print each candidate data
    write_index = 0
    winner_index = 0
    winner = candidate_list[0]

    # Calculate results for each candidate - Note to grader: I limited the decimal places for the % for clarity in print
    for items in candidate_list:
        name = candidate_list[write_index]
        percent = round((votes[write_index]/overall_vote_count)*100,2)
        votes_for_candidate = votes[write_index]
        txt_file.write(f"{name}:  {percent}%  ({votes_for_candidate})\n")

        #Also print to termin al screen
        print(f"{name}:  {percent}%  ({votes_for_candidate})")
        
        #Compare results to determine the winner
        if votes[write_index] > votes[winner_index]:
            winner_index = write_index
            winner = candidate_list[winner_index]
       
        write_index = write_index + 1    
    txt_file.write(f"-------------------------\nWinner: {winner}\n-------------------------\n")

    #Also print to terminal screen
    print(f"-------------------------\nWinner: {winner}\n-------------------------\n")


