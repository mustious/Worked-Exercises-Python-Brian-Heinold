import math

number = int(input("Please enter the your n: "))

sub_sum = 0
for num in range(1, number + 1):
    sub_sum += (1/num)

result = sub_sum - math.log(number)
print(result)
