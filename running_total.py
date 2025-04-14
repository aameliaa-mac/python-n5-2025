# running total - lesson 310 (14/04/25)

# set up items array + total variable
items = [4,9,6,13]
total = 0

# loop four times!
for index in range(4):
    # add current item in items array to total
    total = total + items[index]

# display total!
print(total)

# what is a running total?

# a running total is a sum that is continually updated as you loop through a sequence of numbers
# this technique is useful in many scenarios
# such as calculating the total cost of items in a shopping cart
# finding the sum of all elements in an array
# or calculating rainfall over a period of time.
