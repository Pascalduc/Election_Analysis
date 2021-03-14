#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidates won
# 4. The total number of votes each candidates won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime
dir(datetime)
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)


# Direct filepath
# Assign a variable for the file to load and the path.
# file_to_load = 'Resources\election_results.csv'
# Open the election results and read the file.
# election_data = open(file_to_load, 'r')
# Close the file.
# election_data.close()
# Open close can be replaced by With function
# Open the election results and read the file
# with open(file_to_load) as election_data:
     # To do: perform analysis.
     # print(election_data)

# Indirect filepath
import csv
import os
import numpy
# dir(os)
# dir(os.path)
# join function called chaining
file_to_load = os.path.join("Resources", "election_results.csv")
with open(file_to_load) as election_data:
    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# Write some data to the file.
# outfile.write("Hello World")
# Close the file
# outfile.close()

# Make the code cleaner
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
########################################
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Hello World Again")
##############################################
# Add counties 1st way
     # Write three counties to the file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe, ")
    txt_file.write("Denver, ")
    txt_file.write("Jefferson,")
##########################################
# New line \n
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the election\n---------------------\nArapahoe\nDenver\nJefferson")



#######################################################################
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# Create empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

# If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    
# Determine the percentage of votes for each candidate by looping through the counts.
#  Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage:0.1f}% of the vote.")

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        # print out the winning candidate, vote count and percentage to terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)