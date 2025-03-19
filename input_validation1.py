# lesson 308 - 19/03/25

# get user input
percentage = int(input("Enter Percentage"))

# validate between 0 and 100
while percentage < 0 or percentage > 100:
    print("error, % must be between 0 and 100!!")
    percentage = int(input("please enter a valid percentage!"))
