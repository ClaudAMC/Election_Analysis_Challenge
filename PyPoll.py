# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
import random
import numpy


# INDIRECT PATH TO FILE EXAMPLES

import os

file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Assign a variable for the file to load and the path. #DIRECTMETHOD file_to_load = 'Resources/election_results.csv'

# DIRECT PATH EXAMPLES:

# Open the elcetion results and read the file. #election_data = open(file_to_load, 'r')
# To do: perform analysis.
# Close the file #election_data.close()

# 1. Initialize the  total vote counter

total_votes = 0

# Intialize the candiate options

candidate_options = []

# Initialize the candidate votes dictionary.

candidate_votes = {}

# Winning Candiate and Winning Count Tracker

winning_candidate = ""
winning_count = 0
wining_percentage = 0

# Open the election results and read the file 

with open(file_to_load, encoding='UTF-8') as election_data:

    # To do: perform analysis

    # Read the file object with the reader function.

    file_reader = csv.reader(election_data)

    # Print the header row

    headers = next(file_reader)

    # Print each row in the csv file
    
    for row in file_reader:

        # 2. Add to the total vote count.

        total_votes += 1

        # Print the candidate name from each row

        candidate_name = row[2]

        # if the candidate does not match any existing candidate then..
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidates vote count.
            candidate_votes[candidate_name] = 0
            
        # Add a vote tot that candidates count.
        candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping throuhg the counts.


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrive vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of the vote.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Save the candidate results to out text file.
        txt_file.write(candidate_results)
        
        # Determine the winning vote count and candidate

        # Determine if the votes is greater than the winnning count.

        if (votes > winning_count) and (vote_percentage > wining_percentage):

            # If true then set winning_count = votes and winning_percent = vote_percent

            winning_count = votes
            wining_percentage = vote_percentage

            # And, set the wining candidate equal to the candidates name

            winning_candidate = candidate_name

    # Print winning candidates result to the terminal

    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {wining_percentage:.1f}%\n"
        f"----------------------------\n")
    
    print(winning_candidate_summary)
    
    # Save the winning candidate name to the text file.
    
    txt_file.write(winning_candidate_summary)

    


    # Print candidate list.
    #print("-----------------------------")
    #print(candidate_votes)

    # 3. Print the total votes.
    #print("-----------------------------")
    #print(total_votes)



    # Using the open finction with the 'w' mode we will write data to the file

    # with open(file_to_save, "w") as outfile:

    # Write some data to the file

        # outfile.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")



