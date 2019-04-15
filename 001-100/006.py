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
