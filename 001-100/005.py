#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallestMultiple(value):
    aux = 1
    for i in range(1, value+1):
            for j in range(1, value+1):
                if (aux*j) % i == 0:
                    aux *= j
                    break
    return aux

print(smallestMultiple(20))
