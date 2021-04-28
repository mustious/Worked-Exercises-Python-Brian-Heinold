meal_price = float(input("please enter the price of the meal: "))
tip_percent = float(input("please enter tip percent: "))
tip = meal_price * tip_percent
print(f"The tip amount is {tip}")
print(f"The total amount including tip is {tip + meal_price}")