daily_sales = [5, 67, 4, 54, 4, 23, 54]

# Memory effiecient operations
total_cups = sum(sale for sale in daily_sales if sale > 5) 

print(total_cups)