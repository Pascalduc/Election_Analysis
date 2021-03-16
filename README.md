# Overview of Election Audit

## Project Overview
In this project, we are assisting Tom write a Python script for the Colorado Board of Election to audit the local congressional election.
The goal is for the script to perform the following task:

1. Calculate the total number of votes cast.
2. Return a complete list of candidates who received votes.
3. Calculate the percentage of votes each candidate won.
4. Calculate the total number of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.54.2

## Election-Audit Results
For this election analysis we wrote a Python script to quickly scan through hundreds of thousands of ballots while collecting information about the county where it was cast and the candidate who was picked. We first imported a couple of modules to simplify our code and initialized the data file, the analysis writable file and all the variables.
```
import csv
import os
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}
# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# 2: Track the largest county and county voter turnout.
top_county = ""
top_county_votes = 0
```
We initialized `candidate_options` and `county_options` as an empty list while `candidate_votes` and `county_votes` were set as empty dictionaries in order to match the `key` and the `value`. The counts were set to zero then we opened the data file and ran through the rows with a `for loop` and membership operator to extract the vote for each candidate. 
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # Read the header
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
•	The total vote count was determined with the following code: 
```
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
```
Then printed to the results file:

```
Election Results
-------------------------
Total Votes: 369,711
-------------------------
```
•	Similarly, we looped through the data to extract the vote for each county resulting in a vote count and percentage per county as follow:
```
County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
```
•	With an `if` statement we determined the county with the largest turnout was:
`Largest County Turnout: Denver`
•	There were three candidate with the following vote counts:
```
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
```
•	And the winner of the election was determined also with an if` statement:
```
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
```
```
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------
```

## Election-Audit Summary
This script could be very useful for the election commission since it can be quickly modified to read other data files. All that is needed is to replace the file name with the new one. If the columns are not in the same order, we can easily modify the row[index]. 
```
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")
```
```
        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```
In order to make sure there is no mistakes with the script and that no vote goes uncounted, we could add a few lines of codes to return the sum of votes from each candidate and the sum of votes in each county comparing them to the total votes which was obtain from a row count minus header. The three totals should be equal.
