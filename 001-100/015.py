#Starting in the top left corner of a 2×2 grid, and only beingable to move
#to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
import math
x,y=12,8
print(math.factorial(x+y)/math.factorial(10)**2)
