#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import math
import time

def primeOrd(value):
    num=3
    count=1
    t0 = time.time()
    while count < value:
        aux = round(math.sqrt(num))

        for i in range(2,aux+1):
            if num % i == 0:
                break
            elif i==aux:
                prime=num
                count+=1
                break
        if count!=value:
            num+=2
    t1 = time.time()
    print(t1-t0)
    return num
    
print(primeOrd(10001))
