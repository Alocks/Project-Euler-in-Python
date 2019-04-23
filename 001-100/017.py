#list1[1~9]=1~9
#list2[1~10]=10~19
#list3[1~8]=20,30...90
list1=[0,3,3,5,4,4,3,5,5,4]
list2=[3,6,6,8,8,7,7,9,8,8]
list3=[0,0,6,6,5,5,5,7,6,6]
a,b,c=0,0,0
result=0
teste1=0
teste2=0
for i in range(99):
 aux=len(str(i+1))
 print(i+1)
 if aux ==1 or str(i+1)[:2]=='10':
     a=i
 elif aux ==2:
     
     a=int(str(i+1)[1])
     b=int(str(i+1)[0])
 if b==1:
     result+=list2[a]
 else:
     result+=list3[b]+list1[a]
    
