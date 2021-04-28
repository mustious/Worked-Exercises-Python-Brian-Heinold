number = int(input("please enter a number: "))

divisors = []
for i in range(1, number):
    if number % i == 0:
        divisors.append(i)

print(divisors)