total = 2
x = 1
y = 2
z = 0

while(z < 4000000):
    z = x+y
    x = y
    y = z
    if z % 2 == 0:
        total += z

print(total)
