print("enter a list of numbers seperated by space e.g 23 2 1 3")
numbers_str = input("Enter the numbers: ")
numbers_list = [int(num) for num in numbers_str.split()]

print("Sum: {}".format(sum(numbers_list)))
print(numbers_list[-1])
print(numbers_list[-1::-1])
print(f"{'Yes' if len(numbers_list) == 5 else 'No'}")
print("Number of fives: {}".format(numbers_list.count(5)))
numbers_list.pop()
numbers_list.pop(0)
numbers_list.sort()
print(numbers_list)