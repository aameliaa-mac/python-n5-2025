# 17/03/25 - lesson 307

import random

score = 0

words = ["python", "function", "random", "length", "computer", "program", "variable"]

secret_word = random.choice(words)

guess = str(input("which word are you guessing (python/function/random/length/computer/program/variable)?: "))
