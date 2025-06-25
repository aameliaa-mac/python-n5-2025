# mystery mansion - lesson 319 (25/06/25)

names = ["bedroom", "dining room", "kitchen", "garage"]
description = ["creepy bed and cracked mirror", "dirty plates and blood-stained cloth", "no food in the cupboards, only maggots", "spider web covered antique cars and old childhood memories"]
commands = ["N", "S", "E", "W", "quit", "help"]

name = input("what is your name?: ")
print("welome to mystery mansion,", name, "!")

print("if you head north, you will reach the bedroom. if you head east, you will reach the dining room. if you head south, you will reach the garage. if you head west, you will reach the kicten.")
direction = input("direction (N/S/E/W/quit/help): ")

if direction != "N" and "S" and "E" and "W":
    print("that is not a valid direction. please try again!")
    direction = input("direction (N/S/E/W/quit/help): ")


if direction == "N":
    print("you have arrived into the bedroom. to your left is a creepy bed and to your right is a cracked mirror.")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "S":
    print("you have arrived in the garage. to your left is an old, spider web covered antique car and to your right are boxes overflowing with childhood memories.")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "E":
    print("you have now arrived in the dining room. to your left is a stack of dirty, unwashed plates and to your right is an old table covered in a blood-stained cloth.")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "W":
    print("you have now arried in the kitchen. there are no food in the cupboards, only maggots.")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "help":
    help = ("what do you need help with?: ")
    print("sorry i cannot help with that issue. please contact kirsty scott brown at k.scottydawg@gmail.com. she may not relpy immediately as it is currently the summer holidays.")
    direction = input("direction (N/S/E/W/quit/help): ")

if direction == "quit":
    print("please press the x.")