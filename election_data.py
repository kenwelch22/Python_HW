import csv
import os
path_name = "/Users/kwelch/Downloads/Python_election_data.csv"
file = open(os.path.join(path_name), "rU")
reader = csv.reader(file, delimiter=',')
vote_count = 0
candidate_list = ['Khan', 'Correy', 'Li', "O'Tooley"]
khan_count = 0
correy_count = 0
li_count = 0
o_tooley_count = 0
vote_count_list = []
for row in reader:
    if row[0] == "Voter ID":
        continue
    vote_count += 1
    if row[2] not in candidate_list:
        candidate_list.append(row[2])


    if row[2] == 'Khan':
        khan_count += 1
    elif row[2] == 'Correy':
        correy_count += 1
    elif row[2] == 'Li':
        li_count += 1
    elif row[2] == "O'Tooley":
        o_tooley_count += 1


vote_count_list.append(khan_count)
vote_count_list.append(correy_count)
vote_count_list.append(li_count)
vote_count_list.append(o_tooley_count)

percentage_list = []
for votes in vote_count_list:
    percentage = votes/vote_count
    percentage_list.append(percentage)

vote_winner = max(vote_count_list)

if vote_count_list[0] == vote_winner:
    winner = "khan"
elif vote_count_list[1] == vote_winner:
    winner = "correy"
elif vote_count_list[2] == vote_winner:
    winner = "li"
else:
    winner = "O'Tooley"

print("Election Results" + "\n"
      "Total Votes: " + str(vote_count) + "\n"
      "Khan: " + str(percentage_list[0]) + " (" + str(vote_count_list[0]) + ")" + "\n"
      "Correy: " + str(percentage_list[1]) + " (" + str(vote_count_list[1]) + ")" + "\n"
      "Li: " + str(percentage_list[2]) + " (" + str(vote_count_list[2]) + ")" +  "\n"
      "O'Tooley: " + str(percentage_list[3]) + " (" + str(vote_count_list[3]) + ")" +  "\n"
      "Winner: " + winner)

file = open('election.txt', 'w+')
file.write("Election Results" + "\n"
      "Total Votes: " + str(vote_count) + "\n"
      "Khan: " + str(percentage_list[0]) + " (" + str(vote_count_list[0]) + ")" + "\n"
      "Correy: " + str(percentage_list[1]) + " (" + str(vote_count_list[1]) + ")" + "\n"
      "Li: " + str(percentage_list[2]) + " (" + str(vote_count_list[2]) + ")" +  "\n"
      "O'Tooley: " + str(percentage_list[3]) + " (" + str(vote_count_list[3]) + ")" +  "\n"
      "Winner: " + winner)