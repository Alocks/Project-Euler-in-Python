#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

list = []
pf=600851475143
p=3 
while pf > 1:
    if pf % p == 0:
        pf=pf/p
        list.append(p)
    p+=2

print(list)
        
