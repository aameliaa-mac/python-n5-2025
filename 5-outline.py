
# finished!!

print("outline")
print("=======")

print()
lines = [] # this is an array

lines_in_image = int(input("how many lines are used in the image?: "))
for index in range(lines_in_image):
    newline = input("Enter the next line of ASCII: ")
    lines.append(newline) # this adds the new line to the lines array
print(lines)

count = 0
for line in lines: # for each line in the array
    for index in range(len(line)): # for each character in the line
        if line[index] != " ": # if the character is NOT a space
            count = count + 1 # add 1 to count

print("there are",count,"characters in this image!")