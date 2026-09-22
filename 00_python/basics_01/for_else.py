staff = [("Amit", 16), ("Zara", 13), ("Raj", 12)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is elible for the staff")
        break
else:
    print(f"No one is elible for the staff")