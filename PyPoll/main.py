import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('.', 'Resources', 'election_data.csv')

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0





# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

   
    # Loop through the data
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # Update candidate's vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Output results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and display the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}% ({votes})")

    # Check for the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results")
    txtfile.write("-------------------------")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("-------------------------")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})")

    txtfile.write("-------------------------")
    txtfile.write(f"Winner: {winner}")
    txtfile.write("-------------------------")

print("Results saved to election_results.txt")