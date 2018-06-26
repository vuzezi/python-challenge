import csv
from collections import Counter
import os

csvpath = os.path.join('Resources', 'election_data.csv')

#Read and open the csv election_data file
with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader) 

    # Variables to store percntage for each vote, candidate names and voters count
    votesCount = Counter() 
    candList = [] 
    percentage = [] 
    answer = [] 

    for i in csvreader: 
        candList.append(i[2])

    totalVotes = len(candList)

    for name in candList: 
        votesCount[name] += 1
#Identify the winner
    winner = max(zip(votesCount.values(), votesCount.keys())) 
    names = tuple(votesCount.keys())
    votes = tuple(votesCount.values())

    for x in votes:
        percentage.append((int(x)/totalVotes)*100) 
    
    answer.append('Election Results')
    answer.append('-----------------------')
    answer.append('Total Votes: ' + str(totalVotes))
    answer.append('-----------------------')
    for x in range(len(names)):
        answer.append(names[x] + ': ' + str(round(percentage[x],1)) + '% ' + '(' + str(votes[x]) + ')')
    answer.append('-----------------------')
    answer.append('Winner: ' + winner[1])
    answer.append('-----------------------')

    print("\n".join((answer)))

