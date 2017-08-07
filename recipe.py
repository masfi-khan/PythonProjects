#spicy lemon garlic shrimp
ingredients = ["shrimp", "butter",  "parsley leaves", "salt", "red pepper", "garlic", "lemon juice", "crusty bread"]

instructions = ["(1) Preheat the oven to 375 degrees F. Rinse the shrimp to separate, then arrange in a single layer on a baking sheet.",
"(2) To the bowl of a food processor, add the butter, parsley, salt, red pepper, garlic and lemon juice. Pulse until combined. Sprinkle the cold butter crumbles over the shrimp.",
"(3) Bake until the shrimp is opaque and the butter is hot and bubbly.",
"(4) Serve with hot crusty bread. Peel and eat the shrimp, and then encourage guests to dip the bread into the butter in the bottom of the pan."]

recipe = {"ingredients":ingredients, "instructions":instructions}

#ingredients and instructions within lists, dictionary includes those lists, print values from dictionary based on their keys
#think of "recipe" dictionary as a cookbook, with ingredients and the instructions

for i in range(4):
    print(recipe["instructions"][i])

for i in range(8):
    print(recipe["ingredients"][i])

user_input = input("What ingredient do you want to use?")
if user_input in ingredients:
    print(recipe["instructions"])
else:
    print("A recipe with that ingredient is unavailable.")


    # print(recipe["ingredients"])
    # print(recipe["instructions"][0])
    # print(recipe["instructions"][1])
    # print(recipe["instructions"][2])
    # print(recipe["instructions"][3])
    #simplified with for-loops
    #for-loops run through items in the list; ranges represents amount of items in list; i represents all indices
