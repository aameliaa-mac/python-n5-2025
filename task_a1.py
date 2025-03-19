# input validation (19/03/25) - lesson 308

list = []

test_score = int(input("what is the percentage of your test score?: "))

while test_score < 0 or test_score > 100:
    print("error, % must be between 0 and 100!!")
    test_score = int(input("please enter a valid percentage!"))

list.append(test_score)
print(list)