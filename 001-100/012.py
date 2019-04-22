import math
value=tot=count=aux=0
while count<500:
    count=0
    aux+=1
    tot+=aux
    for i in range(1,(int(math.sqrt(tot)))+1):
        if tot%i==0:
            count+=2
    if(count*count==value):
        count=-1
print(tot)
        
