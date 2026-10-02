users = [
    { "id": 1, "total": 100, "coupon": "P20"},
    { "id": 12, "total": 130, "coupon": "S20"},
    { "id": 122, "total": 140, "coupon": "F20"}
]

discounts = {
    "P20": (0.2, 0),
    "S20": (0.5, 0),
    "F20": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print("xyz")