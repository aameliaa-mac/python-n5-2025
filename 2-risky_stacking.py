
# finished!!

print("risky stacking")
print("==============")

print()

height_of_one_chair_in_cm = int(input("Enter the height of one chair: "))
total_height_of_chair_stack_in_cm = int(input("Enter the total height of the chair stack: "))

print()

total_number_of_chair_legs = int(( total_height_of_chair_stack_in_cm / height_of_one_chair_in_cm ) *  2) * 4

print("Total number of chair legs in the chair stack is: ", total_number_of_chair_legs)