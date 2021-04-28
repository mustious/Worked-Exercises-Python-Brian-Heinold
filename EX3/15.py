import math

for degree in range(0, 350, 15):
    print("{} --- {:.4f} {:.4f}".format(degree, math.sin(degree), math.cos(degree)))