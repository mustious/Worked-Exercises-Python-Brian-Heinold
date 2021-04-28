number = int(input("Please enter the your number: "))

divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(f"Sum of divisors of {number} is {sum(divisors)}")