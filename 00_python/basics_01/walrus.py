# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

# using walrus
value = 13

if(remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")


available_size = ["small", "medium", "Large"]

if(requested_size := input("Enter the size")) in available_size:
    print(f"{requested_size} Size is available")
else:
    print(f"Size is not available")
