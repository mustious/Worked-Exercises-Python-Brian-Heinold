import sys 

number = int(input("Please enter the your number: "))

divisors = []
squares = [0]
for i in range(1, number + 1):
    if i != 1 and squares[-1] < number:
        squares.append(i ** 2)
        
    
    # get the divisors of number
    if number % i == 0:
        divisors.append(i)
        
        if i in squares:
            print("not squarefree")
            sys.exit()
    
print("squarefree")

