# input validation (19/03/25) - lesson 308

list = []

name = str(input("what is your name?: "))
clan = str(input("what clan are you in?: "))

while clan != "stuart" "forbes" "douglas" "gordon":
    print("error, that clan is not accepted! please try again :)")
    clan = str(input("what clan are you in?: "))

list.append(name, clan)
print(list)