# program 3 - investigate and modify (17/03/25) lesson 307

password = input("please enter your password: ")
while len(password) < 8:
    print("error, please try again :) your password must be more than eight letters")
    password = input("please enter your password: ")
print("password accepted!!")

