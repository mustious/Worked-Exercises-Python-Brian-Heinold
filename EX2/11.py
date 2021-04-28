box_width = int(input("Please enter box width: "))
box_height = int(input("Please enter box height: "))

for h in range(box_height):
    if  h == 0 or h == box_height - 1:
        print("*" * box_width)
    else:
        print("*" + " " * (box_width - 2) + "*")2