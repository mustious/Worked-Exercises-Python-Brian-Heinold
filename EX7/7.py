import sys

L_str = input("Enter a list of numbers L: " )
M_str = input("Enter a list of numbers M: ")

L = [int(num) for num in L_str.strip().split()]
M = [int(num) for num in M_str.strip().split()]

result = []

if len(L) != len(M):
    print("L and M must be of same length")
    sys.exit()

for L_i, M_i in zip(L, M):
    result.append(L_i + M_i)

print(result)