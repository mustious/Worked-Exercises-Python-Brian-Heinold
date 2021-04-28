num_fib = int(input("Please enter the number of fibonacci numbers you want: "))

fib = [1, 1]

for i in range(2, num_fib):
    next_fib = sum(fib[-2:])
    fib.append(next_fib)
print(fib)