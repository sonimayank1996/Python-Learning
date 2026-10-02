tea_price_inr = {
    "Masala chai": 40,
    "Green chai": 50,
    "Ginger chai": 140
}

tea_price_usd = {tea:price/80 for tea, price in tea_price_inr.items()}
print(tea_price_usd)