#import os and write csv path
from statistics import mean
import os
import csv

# creathing a path to the budget_data csv file using imported CSV module

csvpath = os.path.join( 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:

    # reading the CSV data file using the csv reader and store in two variabvbles date and revenues

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    budget_list = list(csvreader)

    dates = []
    revenues = []

    #run for loop for every row to track changes in revenue for every month
    for i in budget_list:
        dates.append(i[0])
        revenues.append(int(i[1]))
    
    
    revenue_change = []

    revenue_change = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
    
    #variables to track changes

    max_change = max(revenue_change)
    big_loss = min(revenue_change)
    avg_change = mean(revenue_change)
    total_month = len(dates)
    max_month = None
    loss_month = None

    
    #for loop to find date matching bigest loss/ Biggest gain
    initial_val = None
    for row in budget_list:
        if initial_val is None:
            initial_val = int(row[1])
            continue
        if int(row[1]) - initial_val == big_loss:
            loss_month = row[0]
        initial_val = int(row[1])

    initial_val2 = None
    for row in budget_list:
        if initial_val2 is None:
            initial_val2 = int(row[1])
            continue
        if abs(int(row[1]) - initial_val2) == max_change:
            max_month = row[0]
        initial_val2 = int(row[1])
    

    print("Financial Analysis")
    print("-----------------------------------------------------------------------------")
    print(f"The financial analysis occured over {total_month} months")
    print(f"The average revenue change was ${avg_change}")
    print(f"Greatest Increase in Profit was ${max_change} and occured on {max_month}")
    print(f"Greatest Decrease in Profit was ${big_loss} and occured on {loss_month}")