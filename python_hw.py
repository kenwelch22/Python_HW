import csv
import os
path_name = "/Users/kwelch/Downloads/budget_data.csv"
file = open(os.path.join(path_name),'rU')
reader = csv.reader(file, delimiter =',')
month_count = 0
total_profit = 0
profit_or_loss_list = []
for row in reader:
    if row[0] == "Date":
        continue
    month_count += 1
    profit_float=float(row[1])
    total_profit =total_profit + profit_float
    profit_or_loss_list.append(profit_float)

max_profit_or_loss = max(profit_or_loss_list)
min_profit_or_loss = min(profit_or_loss_list)
avg_profit = total_profit/month_count

print("months: " + str(month_count) + "\n" "total_profit: " + str(total_profit) + "\n" "max_profit: " + str(max_profit_or_loss) + "\n" "min_profit: " + str(min_profit_or_loss) + "\n" "avg_profit: " + str(avg_profit))

file = open('manipulate_csv.txt', 'w+')
file.write("months: " + str(month_count) + "\n" "total_profit: " + str(total_profit) + "\n" "max_profit: " + str(max_profit_or_loss) + "\n" "min_profit: " + str(min_profit_or_loss) + "\n" "avg_profit: " + str(avg_profit))

