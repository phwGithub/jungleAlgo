x=input("")

if len(x) == 1 or len(x) == 2:
    res = int(x)
elif len(x) == 3:
    res = 99
    res2 = 0
    for i in range(100,int(x)+1):
        i = str(i)
        if int(i[2]) - int(i[1]) == int(i[1]) - int(i[0]):
            res2 += 1
    res += res2
else:
    res = 144

print(res)