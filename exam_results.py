# exam results - lesson 317 (18/06/25)

english = int(input("mark for english (%): "))
maths = int(input("mark for maths (%): "))
art = int(input("mark for art (%): "))
computing = int(input("mark for computing (%): "))

sum = english + maths + art + computing
average = sum / 4

print("english:", english,"%")
print("maths:", maths,"%")
print("art:", art,"%")
print("computing:", computing,"%")
print("average mark:", average,"%")