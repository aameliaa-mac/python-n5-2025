
# finished!!

print("can packing")
print("===========")

print()

length_of_square_packs = int(input("enter the length of square packs being made: "))
special_offer = input("is a special offer running? (y/n): ")
additional_free_rows = int(input("please enter the number of additional rows included for free: "))

print()

width_of_square_packs = length_of_square_packs

if length_of_square_packs > 0 and length_of_square_packs < 10:
    number_of_tin_cans = length_of_square_packs * width_of_square_packs

if special_offer == "y":
    width_of_square_packs = width_of_square_packs + additional_free_rows
    number_of_tin_cans = length_of_square_packs * width_of_square_packs

print("the number of cans in the pack is: ", str(number_of_tin_cans))
