weight_kg = float(input("Enter your weight in KG: "))

print(weight_kg)
while weight_kg == 0:
    print("Invalid value of weight == 0")
    print("try again")
    weight_kg = float(input("Enter your weight in KG: "))

weight_pounds = weight_kg * 2.2
print("The weight in pounds is {}".format(weight_pounds))
