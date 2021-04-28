pattern = [1, 2]
for i in range(8):
    if i % 2 == 0:
        print(pattern*4)
    else:
        print(pattern[-1::-1]*4)
