# running total task 1 - lesson 310 (14/04/25)

total = 0

for counter in range (0,12):
    monthly_savings = float(input("what are your savings this month?: "))
    total = total + monthly_savings
    print("your savings so far this year is:", total)
