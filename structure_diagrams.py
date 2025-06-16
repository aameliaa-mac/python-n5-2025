# lesson 314 - 21/05/25

pricepermile = 0
startmiles = 0

for index in range (1,5):
    currentmiles = int(input("what is the mileage at your current charging station?: "))
    rating = int(input("what is your valid kW rating at your current charging station? (7/22/50): "))

    while rating != 7 and rating != 22 and rating != 50:
        print("error...")
        rating = int(input("what is your valid kW rating at your current charging station? (7/22/50): "))

    if rating == 7:
        pricepermile = 0
    elif rating == 22:
        pricepermile = 0.005
    else:
        pricepermile = 0.01
    
    milestravelled = currentmiles - startmiles
    startmiles = currentmiles

    cost = pricepermile * milestravelled

    print("the cost of this stage of the journey was: £", cost)