import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')


total_months = 0
net_total = 0
changes = []
months = []
greatest_increase=["",0]
greatest_decrease=["",0]

# Read CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #firstmonth
    first_row=next(csvreader)
    total_months+=1 # total_months = total_months + 1
    net_total+=int(first_row[1])
    previous_profit_loss=int(first_row[1])
    

    # Iterate through rows
    for row in csvreader:
        month=row[0]
        profit_loss=int(row[1])

        total_months+=1
        net_total+=profit_loss

        change = profit_loss - previous_profit_loss

        changes.append(change)
        months.append(month)    

        if change>greatest_increase[1]:
            greatest_increase[0]=month
            greatest_increase[1]=change

        if change<greatest_decrease[1]:
            greatest_decrease[0]=month
            greatest_decrease[1]=change

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

    # Calculate average change
    average_change = sum(changes) / len(changes)

   
    # Print results
    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total: ${net_total}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")










