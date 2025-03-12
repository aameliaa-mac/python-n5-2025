# this is an example of a conditional loop

userscore = int(input("Enter your score: "))

while userscore<0 or userscore>9999:
    print("Invalid score. Try again.")

userscore = int(input("Enter your score: "))

