#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

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
