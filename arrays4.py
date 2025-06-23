# traversing a 1D array - lesson 318 (23/06/25)

# Create a program that contains an array of 7 daily temperatures (in celsius). 
# Traverse the 1D array to calculate and display the average temperature (sum of 7 days/7).

temp = [21,22,19,24,21,23,22]

average = sum(temp)
average = round(average / 7,1)

print(temp)
print("average temperature (celsius): ", average)