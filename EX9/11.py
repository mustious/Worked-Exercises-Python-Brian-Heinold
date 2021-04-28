import random

zeros = [[0] * 5 for _ in range(5)]

print(zeros)

indices = []

for row in range(0,5):
    for col in range(0,5):
        indices.append([row, col])

selected_indices_10 = random.choices(indices, k= 10)

for row, col in selected_indices_10:
    zeros[row][col] = 1

print(zeros)