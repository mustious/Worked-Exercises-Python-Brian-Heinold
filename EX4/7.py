first_number = float(input("please enter the first number: "))
second_number = float(input("please enter the second number: "))

if (first_number - second_number) <= 0.001:
    print("Close")
else:
    print("Not close")