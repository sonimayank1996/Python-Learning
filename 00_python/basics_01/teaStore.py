amount = int(input("Enter the order amount"))

delivery_fees = 0 if amount > 300 else 30

print(f"Delivery Fees: {delivery_fees}")