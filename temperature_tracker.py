# temperature tracker - lesson 309 (24/03/25)

temp = []

for counter in range (0,5):
    temperature = int(input("what is your temperature?: "))
    while temperature < -20 or temperature > 50:
        print("your temperature is not accepted, please try again!")
        temperature = int(input("what is your temperature?: "))
    temp.append(temperature)

average = (temp[0] + temp[1] + temp[2] + temp[3] + temp[4]) / 5

print(temp)
print("your average temperature is:", average, "°C")