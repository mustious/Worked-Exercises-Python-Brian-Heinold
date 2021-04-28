a_list = [1, 1, 2, 3, 4, 3, 0, 0]

unique_list = []

for element in a_list:
    if element not in unique_list:
        unique_list.append(element)

print(unique_list)