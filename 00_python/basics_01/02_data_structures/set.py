#Set -> Mutable data type - why ? -> Answer: Because we can change the values of set after creation.

essential_ingredients = {"water", "milk", "tea"}
optional_ingredients = {"sugar", "milk", "clove"}

all_spices = essential_ingredients | optional_ingredients  #union of two sets
print(f"All spices are:- {all_spices}")

common_spices = essential_ingredients & optional_ingredients  #intersection of two sets
print(f"Common spices are:- {common_spices}")

only_essential_spices = essential_ingredients - optional_ingredients  #difference of two sets
print(f"Only essential spices are:- {only_essential_spices}")