
# predefined functions (17/03/25) lesson 307



# example 1: the random module
# provides functions for generating random numbers!

import random
# generates a random float between 0 and 1!!

print(random.random())  # output: something like 0.23456789!!
# generates a random integer between two values (inclusive)!!

print(random.randint(1, 10))  # output: a number between 1 and 10!!
# chooses a random element from a sequence

fruits = ['apple', 'banana', 'orange', 'grape']
print(random.choice(fruits))  # output: one of the fruits



# example 2: the round function
# the round function rounds a number to a specified number of decimal places (defaults to 0)

# basic rounding
print(round(3.14159))  # output: 3
print(round(2.718))    # output: 3

# rounding to specific decimal places
print(round(3.14159, 2))  # output: 3.14
print(round(2.718, 1))    # output: 2.7

# rounding negative numbers
print(round(-2.5))  # output: -2



# example 3: the len function
# the len function returns the number of items in an object (like a string or a 1D array)

# string example
text = "Hello Python"
print(len(text))  # output: 12

# list example
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # output: 5

# fixed loop example
for index in range(0, len(numbers)): # loops 5 times
     print(numbers[index]) # outputs current number in 1D array
