# shopping calculator programming challenge - lesson 317 (16/06/25)

items = []
costs = []  

for counter in range(3):
    food = input("what shopping item are you buying?: ")
    price = float(input("how much does that item cost?: £"))  
    quantity = int(input("how much are you purchasing?: "))  

    items.append(food)
    costs.append(price * quantity)  

total = sum(costs)  

print(items)
print("your total is £", total)
