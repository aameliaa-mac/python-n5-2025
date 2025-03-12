
# program 4 - investigate and modify (12/03/25)

rightnumber = 11
guess = 1
number = int(input("guess a number: "))

while (guess < 5) and (number != rightnumber):
  print("not right. try again!")
  number = int(input("guess a number: "))
  guess = guess + 1

if number == rightnumber:
  print("well done! you guessed the right number :)")