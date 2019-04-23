x = 1000000
tot= 0
result = 0
for i in range(int(x/1.25),x):
  count = 0
  num = i
  while num > 1:
    if num % 2 == 0:
      num = num//2
    else:
      num = 3*num+1
    count += 1
  if count>tot:
    tot = count
    result = i
print(result)
