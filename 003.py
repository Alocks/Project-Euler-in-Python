list = []
pf=600851475143
p=3 
while pf > 1:
    if pf % p == 0:
        pf=pf/p
        list.append(p)
    p+=2

print(list)
        
