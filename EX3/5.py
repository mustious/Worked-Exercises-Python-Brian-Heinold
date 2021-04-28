from random import randint


random_gen_numbers = [] # list of randomly generated numbers

for n in range(1, 51):
    a = randint(1, n + 1) # a randomly generated number between 1 and n+1
    random_gen_numbers.append(a)

print(random_gen_numbers)