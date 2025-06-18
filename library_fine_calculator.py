# library fine calculator - lesosn 317 (18/06/25)

# Stores the number of days a book is overdue
# The fine is £0.50 per day
# If the fine exceeds £5, add an additional £2 processing fee
# Calculate and display the total fine

numberofdays = int(input("how many days is your book overdue for?: "))

fine = numberofdays * 0.5

if fine > 5:
    fine = fine + 2

print("your fine is: £", fine)