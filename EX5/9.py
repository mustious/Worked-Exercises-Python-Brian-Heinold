perfect_sq = [num ** 2  for num in range(1, 20) if (num ** 2) <= 1000]
perfect_3 = [num ** 3  for num in range(1, 20) if (num ** 3) <= 1000]
perfect_5 = [num ** 5  for num in range(1, 20) if (num ** 5) <= 1000]

total_numbers = perfect_3 + perfect_5 + perfect_sq
all_len = len(set(total_numbers))
print("Number of integers that are not perfect squares, perfect cubes or \
perfect fifth powers are: {}".format(1000 - all_len))