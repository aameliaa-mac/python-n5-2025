# 12/3/25 lesson 306

h = 0
a = 0
period = 1

while period <= 3:
    # print scoreboard here
    print("___________________________")
    print("home -", h," away -", a,)
    print("period -", period)
    print("___________________________")

    option = input("enter (h)ome, (a)way or (p) to end a period: ")
    while option != "h" and option != "a" and option != "p":
        print("this is not an option. please try again!")
        option = input("enter (h)ome, (a)way or (p) to end a period: ")
    if option == "p":
        period = period + 1
    if option == "h":
        h = h + 1
    if option == "a":
        a = a + 1
