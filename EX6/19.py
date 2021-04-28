number_str = input("please enter a large number: ")

len_str = len(number_str)
new_str = ""
for i in range(len_str, 0, -3):
    if i <= 3:
        new_str = number_str[: i] + new_str
    else:
        new_str = "," + number_str[i-3:i+1] + new_str

print(new_str)
