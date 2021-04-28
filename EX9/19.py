import random

numbers_to_9 = list(range(1, 10))

matrix_9_9 = []
for _ in range(0, 9):
    random.shuffle(numbers_to_9)
    matrix_9_9.append(numbers_to_9)

print(matrix_9_9)

