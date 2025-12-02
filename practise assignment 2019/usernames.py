import random

endings = [0,1,2,3,4]

endings[0] = 'ing'
endings[1] = 'end'
endings[2] = 'axe'
endings[3] = 'gex'
endings[4] = 'goh'

number = int(input("how many usernames should be made? "))

for counter in range (number):
    three = input("first three letters of students name: ")
    length = len(three)
    if length != 3:
        print("error. length of inputted name is incorrect.")
        three = input("first three letters of students name: ")
    #end = random.choice(endings)
    end = random.randint(0,4)
    print("new username is: ", three + endings[end])


