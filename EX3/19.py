height = int(input("please enter the height of rectangle: "))
width = int(input("please enter the width of rectangle: "))

start = 0
for h in range(height):
    line_numbers = []
    for w in range(width):
        if start > 9:
            start = 0
        line_numbers.append(str(start))
        start += 1
    print(" ".join(line_numbers))
