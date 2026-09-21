snackk = input("Enter your preferred snank").lower()

print(f"user said: {snackk}")

if snackk == "cookies" or snackk == "samose":
    print("Order done", snackk)
else:
    print("Out of stock")