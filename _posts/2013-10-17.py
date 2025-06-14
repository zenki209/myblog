from collections import defaultdict
from datetime import datetime



A = [100,100,100,-10]
D = ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"] #230

A1 = [180, -50, -25, -25] 
D1 = ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"] #25

balance = 0
monthly_payments = defaultdict(list)

for amount, date in zip(A1,D1):
    balance += amount
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    month = date_obj.month

    if amount < 0:
        monthly_payments[month].append(amount)

print( balance)
print(monthly_payments)
total_fees = 5 * 12
for month,payments in monthly_payments.items():
    if len(payments) >= 3 and sum(payments) <= -100:
        total_fees -= 5
balance -= total_fees

print(balance)

# date_string = "2020-12-31"
# date_object = datetime.strptime(date_string, "%Y-%m-%d")
# print(date_object)