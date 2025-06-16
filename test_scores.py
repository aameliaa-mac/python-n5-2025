# running total task 2 - lesson 310 (16/04/25)

total = 0

for counter in range (0,5):
    test_score = float(input("what did you get in your test? (out of 100): "))
    total = total + test_score
    print("your test scores added up so far are:", total)

if total > 250:
    print("well done! you passed the overall test :)")
else:
    print("you failed the overall test...")