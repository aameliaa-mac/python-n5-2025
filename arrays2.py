# program 2 - investigate and modify

name = []

for counter in range (0,3):
    firstname = input("please enter your first name: ")
    surname = input("please enter your surname: ")

    fullname = firstname + " " + surname # called concatenation - adds strings together 
    name.append(fullname) # append means add on

print(name)

# you use a fixed loop to make this run thrice - line 5