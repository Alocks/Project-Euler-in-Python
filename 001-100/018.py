def tenPow(value,x,y):
    list=[3,7]
    result=y*(value/10) #How many times 1-9 occurs in hundred
    result+=x*((value/100)-1)#how many times 1-99 occurs
    result+=list[1]*900 #How many times 100 occurs
    result+=list[0]*891 #how many times and occurs
    return result

#Discovering total of 1~99 because the only issue is 10~19 to make a pattern
dict={1:[len('one'),len('two'),len('three'),len('four'),len('five'),len('six'),
         len('seven'),len('eight'),len('nine')],

      2:[len('ten'),len('eleven'),len('twelve'),len('thirteen'),len('fourteen'),
         len('fifteen'),len('sixteen'),len('seventeen'),len('eighteen'),len('nineteen')],

      3:[len('twenty'),len('thirty'),len('forty'),len('fifty'),len('sixty'),
         len('seventy'),len('eighty'),len('ninety')]
      }

y=sum(dict[1]) #Will use in tenPow to count how many times appears for 100,1000,etc..
x=sum(dict[2])+y*9 #1~9 appears 9 times from 1~99, and 10~19 only appears once
x+=(sum(dict[3])*10) #every tens repeats 10 times from 1~99
#Finally, discovering 100~999
print(tenPow(10**3,x,y))
