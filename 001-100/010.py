import math

value=2000000
array=[2]
num=3
while num < value:
    aux = round(math.sqrt(num))
    for i in range(2,aux+1):
            if num % i == 0:
                break
            elif i==aux:
                array.append(num) 
                break
    num+=2
print(sum(array))
