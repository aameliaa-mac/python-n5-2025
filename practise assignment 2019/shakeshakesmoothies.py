# 2025 nat5 assignment 

import random

mystery = ["apple", "banana", "blueberry", "kiwi", "mango", "orange", "peach", "pineapple", "raspberry", "strawberry"]

fruitselections = []

counter = 0

fruit = input("enter chosen fruit: ")
fruitselections.append(fruit)
counter = counter + 1

decision = input("do you want to add another fruit? (Y or N): ")

while decision == "Y" and counter < 6: 
    fruit = input("enter chosen fruit: ")
    fruitselections.append(fruit)
    counter = counter + 1
    decision = input("do you want to add another fruit? (Y or N): ")

if decision == "Y" and counter >= 6:
    print("you cannot add any more fruits.")

mysteryfruit = random.choice(mystery)

print("the fruits you entered were: ")
print(fruitselections)

print("the mystery fruit is", mysteryfruit)
counter = counter + 1

if counter < 3:
    print("you should make a milkshake.")

if counter == 3 or counter == 4:
    print("you should make a smoothie.")

else:
    print("you should make a fruit juice.")