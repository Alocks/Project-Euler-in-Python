def maxPolindrom(value):
    arr = []
    x = (len(str(value)))
    if (x > 1):
        x = int(('9')*(x-1))
    else:
        x = 9
           
    for i in range(value, x , -1):
        for j in range(value, x, -1):
            res = i * j
            if str(res) == str(res)[::-1]:
                arr.append(res)
    maxPoli = max(arr)
    print(arr)
    return maxPoli

print(maxPolindrom(999))
