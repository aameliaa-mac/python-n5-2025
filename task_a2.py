# input validation (19/03/25) - lesson 308

name = str(input("what is your name?: "))
age = int(input("how old are you?: "))

while age < 11 or age > 18:
    print("error, your age is not accepted!! please try again :)")
    age = int(input("how old are you?: "))

print("welcome to the kirsty scott brown talent show! we hope you enjoy :)")