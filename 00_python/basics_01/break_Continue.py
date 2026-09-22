flavours = ["Tulsi", "out of stock",  "Lemon", "Discountinue", "Ginger"]

for flavour in flavours:
    if flavour == "out of stock":
        continue   #skip
    if flavour == "Discountinue":
        break
    print(f"Flavour is the {flavour}")