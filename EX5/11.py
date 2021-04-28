number = int(input("Please enter your number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("{}! = {}".format(number, factorial))