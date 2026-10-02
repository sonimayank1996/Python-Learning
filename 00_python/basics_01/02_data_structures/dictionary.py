#Dictionary -> Mutable data type - why ? -> Answer: Because we can change the values of dictionary after creation.
# why we use dictionary ? -> Answer: Because we can store key value pair in dictionary.

chai_order = dict(type="Ginger Tea", customer="Chai Lover", quantity=2)
print(f"Chai order is:- {chai_order}")

chai_recipe = {}
chai_recipe["water"] = "1 cup"
chai_recipe["milk"] = "1 cup"
print(f"Chai recipe is:- {chai_recipe}")

del chai_recipe["milk"]
print(f"Chai recipe is:- {chai_recipe}")

print(f"Chai recipe is:- {chai_recipe.get('water')}")
print(f"Chai recipe is:- {chai_recipe.get('milk', 'Milk is not present in chai recipe')}")

# print(f"Chai recipe is:- {chai_recipe.keys()}")
# print(f"Chai recipe is:- {chai_recipe.values()}")
# print(f"Chai recipe is:- {chai_recipe.items()}")

last_item = chai_recipe.popitem()
print(f"Last item is:- {last_item}")