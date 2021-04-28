count = 0
for i in range(1, 101):
    num_sq = i ** 2

    if i % 10 == 1:
        count += 1
print("Count of number squares ending with 1 is {}".format(count))