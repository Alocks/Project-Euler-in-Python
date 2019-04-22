#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def findPol(result):
    for i in range(1, round(result/3)):
          for j in range(i+1, round(result/2)):
              k=result-i-j
              if i*i + j*j == k*k:
                  return i*j*k
                
print(findPol(1000))
