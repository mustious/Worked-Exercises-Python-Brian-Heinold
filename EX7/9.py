import random

a_dice = range(1, 7)

results = {}
for _ in range(10000):
    dice_1 = random.choice(a_dice)
    dice_2 = random.choice(a_dice)
    sum_dice_values = dice_1 + dice_2
    if sum_dice_values not in results:
        results[sum_dice_values] = 1
    else:
        results[sum_dice_values] += 1

# calculate percentage
for k, v in results.items():
    print("percentage of rolls to be {}: {:.2f}".format(k, (v/10000)*100))