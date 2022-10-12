# Import os module
import os
# Import csv module
import csv

# File to be loaded
load_file = os.path.join('.', 'Resources', 'election_data.csv')

# Open election data file
with open(load_file) as election_results:
    # csv.reader with delimiter specified for csv
    electiondata = csv.reader(election_results, delimiter=',')
    # print(electiondata) 

    # Read the header of election data file
    header = next(electiondata)
    # print(header)

    # Set the inital vote count to 0
    total_votes = 0
    # Candidate list to hold names
    candidate_list = []
    # Dictionary to hold the votes per candidate
    candidate_votes = {}
    # Variable to hold candidate's vote percentage
    percent_votes = []

    # Set the % & win count 
    winner_percent = 0
    candidate_winner = ""
    win_counter = 0
    
    # Read each row of data after the header
    for row in electiondata:
        # Add to the total vote count
        total_votes += 1
        # Candidate's name
        candidate_name=row[2]
        # If the candidate's name is unique
        if candidate_name not in candidate_list:
            # Append the candidate list & add candidate name
            candidate_list.append(candidate_name)
            # print(total_votes)
            candidate_votes[candidate_name] = 0
    # Start counting individual candidate votes
        candidate_votes[candidate_name] +=1
    print("Election Results") 
    print("-----------------")
    print("Total Votes: " + str(total_votes)) 
    print("-----------------")    

    # Count the votes for each candidate
    for candidate_name in candidate_votes:
        # Add vote count for candidate. 
        votes = candidate_votes[candidate_name]
        # print(votes)

        # Calculate the percentage of votes. Tutor aid for float & print
        percent_votes = float(votes)/float(total_votes)*100 
        print(f"{candidate_name}: {percent_votes:.3f}% ({votes})\n")

        # Win count 
        if (votes > win_counter): 
            win_counter = votes
            winner_percent = percent_votes
            candidate_winner = candidate_name
            #print(candidate_winner)
            #print(candidate_votes)
print("----------------")
print("Winner: " + candidate_winner)  
print("----------------")

# Input into terminal
# python main.py >output.txt
# ls
# cat output.txt