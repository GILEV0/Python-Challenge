# Import os module
import os
# Import csv module
import csv
import statistics

# File to be loaded
budget_file = os.path.join('.', 'Resources', 'budget_data.csv')

# Open budget data file
with open(budget_file) as finance_records:
    # csv.reader with delimiter specified for csv
    budgetdata = csv.reader(finance_records, delimiter=',')
    # print(budgetdata) 

     # Read the header of budget data file
    header = next(budgetdata)
    # print(header)

    #Set variables
    total_months = 0
    net_PL = 0
    PL_change = []
    PL_change_list = []
    greatest_decrease = ["", 9999999999999999999]
    greatest_increase = ["", 0]
    peak_month = ''
    low_month = ''
    per_month_change = []

    first_row = next(budgetdata)
    total_months += 1
    net_PL += int(first_row[1])
    prev_net = int(first_row[1])

    #Loop through to find total months
    for row in budgetdata:

        #Count the total of months
        total_months += 1
        # print(total_months)

        # Calculate the Net profit/loss over the entire period
        net_PL += int(row[1])      
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        PL_change_list += [net_change]
        per_month_change += [row[0]]

         #The greatest increase in revenue (date and amount) over the entire period
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        #The greatest decrease in revenue (date and amount) over the entire period
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

        # PL_change_list.append(int(row[1]))

    # Month to month change
for i in range(len(PL_change_list)-1):
    PL_change = (PL_change_list[i+1] - PL_change_list[i])
    per_month_change.append(PL_change)

# PL_ave = statistics.mean(per_month_change)
PL_ave = sum(PL_change_list) / len(PL_change_list)

print("Financial Analysis")
print("----------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(net_PL))
print("Average Change: $" + str(round(PL_ave, 2)))
print("Greatest Increase in Profits: " + str(greatest_increase[0]) + "  ($" + str(greatest_increase[1]) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + "  ($" + str(greatest_decrease[1]) + ")")

# set the output of the text file
# Input into terminal
# python main.py >output.txt
# ls
# cat output.txt
# budgetanalysispath = os.path.join("./PyBank","Analysis","output.txt")
