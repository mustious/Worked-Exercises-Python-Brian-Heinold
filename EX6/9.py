number = int(input("Enter a number:"))

for n in range(number):
    spaces = " " * n
    print(spaces + str(n+1))
