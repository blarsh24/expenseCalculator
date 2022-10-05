import csv
from datetime import date

dt = date.today()
dt = dt.strftime("%m/%d/%y")
filename = "expenses.csv"

costs = []
total = 0
status = True

with open(filename, "a", newline="") as file:
    csvwriter = csv.writer(file)
    while status == True:

        expense = float(input("How much did you spend? Enter 0 to exit. "))

        costs.append(expense)

        if expense == 0:
            costs.pop()
            total = round(sum(costs), 2)
            average = round(total / len(costs), 2)
            print(f"The total you spent today was: {total}")
            print(f"Your average transaction total today was: {average}")
            status = False
        else:
            csvwriter.writerow([dt, expense])

file.close()
