# recipe scalar - lesson 317 (18/06/25)

# Stores ingredients for a chocolate chip cookie recipe that serves 4 people 
# (flour in grams, butter in grams, sugar in grams, number of eggs, chocolate chips in grams, vanilla in teaspoons)
# Work out the scaling factor as the user wants to cook for 6 people instead
# Scale all ingredients proportionally using the calculated factor
# Display the new ingredient amounts

flour4 = 40
butter4 = 20
sugar4 = 35
eggs4 = 4
chips4 = 20
vanilla4 = 2

flour6 = (flour4 / 4) * 6
butter6 = (butter4 / 4) * 6
sugar6 = (sugar4 / 4) * 6
eggs6 = (eggs4 / 4) * 6
chips6 = (chips4 / 4) * 6
vanilla6 = (vanilla4 / 4) * 6 

print("flour (grams): ", flour6)
print("butter (grams): ", butter6)
print("sugar (grams): ", sugar6)
print("eggs: ", eggs6)
print("chocolate chips (grams): ", chips6)
print("vanilla (teaspoons): ", vanilla6)
