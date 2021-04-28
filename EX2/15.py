a_height = int(input("please enter the height of A: "))

mid_height = int(a_height/2)

for h in range(0, a_height):
    if h == 0:
        a = "*"
        print("{0:^40}".format(a))
    elif h == mid_height:
        a = "*" + "*" * (h*2 - 1) + "*"
        print("{0:^40}".format(a)) 
    else:
        a = "*" + " " * (h*2 - 1) + "*" 
        print("{0:^40}".format(a))