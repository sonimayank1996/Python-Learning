fav_chai = [
    "Masala chai" , "Lemon chai", "Ginger chai", "Elaiychi chai",
    "Lemon chai", "Ginger chai"
]

# unique_chai = { chai for chai in fav_chai }
unique_chai = { chai for chai in fav_chai if len(chai) > 12 }

print(unique_chai)

recipes = {
    "Masala chai" : ["ginger", "cardamom", "clove"],
    "Elaichy chai" : ["cardamom", "milk"],
    "Spicy chai" : ["ginger", "black pepper", "clove"]
}

unique_spices  = { spice for ingredients in recipes.values() for spice in ingredients}

print("unique spices", unique_spices)