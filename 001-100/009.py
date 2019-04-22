def findPol(result):
    for i in range(1, round(result/3)):
          for j in range(i+1, round(result/2)):
              k=result-i-j
              if i*i + j*j == k*k:
                  return i*j*k
                
print(findPol(1000))
