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

import csv
dir(csv)
# use the funtion 'reader'
# other useful modules
import random
import numbers

# Assign a variable for the file to load and the path.
file_to_load = 'Ressources\election_results.csv'

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
# Close the file.
#election_data.close()
# Open close can be replaced by With function
# Open the election results and read the file
with open(file_to_load) as election_data:
     # To do: perform analysis.
     print(election_data)

# Indirect filepath
import csv
import os
dir(os)
dir(os.path)
# join function called chaining
file_to_load = os.path.join("Ressources", "election_results.csv")
with open(file_to_load) as election_data:
    # Print the file object.
     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()

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

########################################
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
####################