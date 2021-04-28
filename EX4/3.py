temp = float(input("please enter temperature: "))

if temp < -273.15:
    print("Temperature is invalid because of absolute zero")
elif temp == -273.15:
    print("absolute temperature is 0")
elif temp > -273.15 and temp < 0:
    print("temperature is below freezing")
elif temp == 0:
    print("temperature is at freezing point")
elif temp > 0 and temp < 100:
    print("temperature is in normal range")
elif temp == 100:
    print("temperature is at the boiling point")
else:
    print("temperature is above boiling point")
