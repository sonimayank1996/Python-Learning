#List -> Mutable data type - why ? -> Answer: Because we can change the values of list after creation.
masala_list = ["onion", "tomato", "potato", "chilli"]
masala_list.append("ginger")
print(f"Masala list is:- {masala_list}")
masala_list.remove("tomato")
print(f"Masala list is:- {masala_list}")

spices = ["cumin", "coriander", "turmeric"]
masala_list.extend(spices)
print(f"Masala list is:- {masala_list}")

#indexing of list
spices.insert(1, "fennel")
print(f"Spices list is:- {spices}")

last_spice = spices.pop()
print(f"Last spice is:- {last_spice}")

print(f"Spices list is:- {spices}")
spices.reverse()
print(f"Spices list is:- {spices}")

spices.sort()
print(f"Spices list is:- {spices}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Max sugar level is:- {max(sugar_levels)}")
print(f"Min sugar level is:- {min(sugar_levels)}")

base_liquids = ["water", "milk", "tea"]
extra_liquids = ["coffee", "juice"]
# overloading of + operator for list concatenation
full_liquids = base_liquids + extra_liquids
print(f"Full liquids list is:- {full_liquids}")

strong_tea = ["black tea"] *3
print(f"Strong tea list is:- {strong_tea}")
strong_coffee = ["black coffee", "latte"] *3
print(f"Strong coffee list is:- {strong_coffee}")

raw_spicy = bytearray(b"spicy")
print(f"Raw spicy is:- {raw_spicy}")