x=999
y=1
lista1=[]
lista2=[]
for i in range(x,y,-1):
    for j in range(x,y,-1):
        tot=j*i
        st1= str(tot)
        a = len(st1)
        if (a %2==0):
            a=int((a/2)-1)
            b=a+a+1            
            st2=st1[:a+1]
            st1=st1[a+1:(len(st1))][::-1]
            if st1 == st2:
                lista1.append('{}*{} = {}'.format(i,j,tot))
                lista2.append(tot)

print(lista1)
print(lista2)
