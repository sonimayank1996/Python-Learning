size = input("Enter the size of cup").lower()

print(f"Size choiced by user: {size}")

if size=="small":
    print(f"Price is 10")
elif size == "medium":
    print(f"Price is 15")
elif size == "large":
    print(f"Price is 20")
else:
    print(f"Unknown cup size")