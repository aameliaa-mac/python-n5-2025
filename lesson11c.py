# lesson 305 - selection statements

number_of_badges = int(input("how man badges are you wanting to order?"))

if number_of_badges > 150:
    total_price = number_of_badges * 0.25 * 0.9
    print("your total price, including your discount is: ", total_price)

else:
    price = number_of_badges * 0.25
    print("your total price is: ", price)