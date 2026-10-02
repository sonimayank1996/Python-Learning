#Tuples -> Immutable data type - why ? -> Answer: Because we can't change the values of tuple after creation.
masala = ("onion", "tomato", "potato", "chilli")
(value1, value2, value3, value4) = masala
print(f"Value is:- {value1} {value2} {value3} {value4}")

ginger_ratio, cadramom_ratio, clove_ratio = 1, 2, 3
print(f"Ginger ratio is:- {ginger_ratio} {cadramom_ratio} {clove_ratio}")
ginger_ratio, cadramom_ratio, clove_ratio = clove_ratio, cadramom_ratio, ginger_ratio
print(f"Ginger ratio is:- {ginger_ratio} {cadramom_ratio} {clove_ratio}")

#membership
print(f"Is onion present in masala:- {'onion' in masala}")