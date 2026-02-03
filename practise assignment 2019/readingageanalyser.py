# reading age analyser - assignment 2021

total = 0
average = 0
words = []

numberofwords = int(input("number of words in a sentence: "))

if numberofwords>20:
    print("inavlid number of words. please try again.")
    numberofwords = int(input("number of words in a sentence: "))

for index in range (numberofwords):
    nextword = str(input("next word in sentence: "))
    words.append(nextword)
    wordlength = len(nextword)
    total = total + wordlength

average = total / numberofwords
roundedaverage = round(average,2)

for index in range (numberofwords):
    print(words[index])

print("the average word length is:", average)

if roundedaverage < 5:
    print("short words - suitable for junior readers.")
if roundedaverage >=5 and roundedaverage <=7:
    print("medium words - suitable for teen readers.")
if roundedaverage > 7:
    print("long words - suitable for senior readers.")