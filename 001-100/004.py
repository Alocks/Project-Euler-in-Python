#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def is_pali(value):
    return str(value) == str(value)[::-1]

limit_x=999
limit_y=100
array=[]

while(True):
    for i in range(limit_x, limit_y, -1):
        for j in range(limit_x, limit_y, -1):
            tot=i*j
            if is_pali(tot):
                array.append(tot)
                break
    break

print(max(array))
