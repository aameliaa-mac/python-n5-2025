# running total - lesson 310 (14/04/25)

# set total to 0
total = 0

# loop 7 times
for index in range(7):
    # get today's rainfall from user
    rainfallToday = float(input("Enter rainfall today (mm): "))
    # add rainfallToday to total
    total = total + rainfallToday

# display total rounded to 2 decimal places
print(round(total,2))
