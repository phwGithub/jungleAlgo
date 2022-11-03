cntT = int(input(""))
listX = input("").split(' ')


cnt = 0
if not cntT == 0:
    for i in range(cntT):
        item = int(listX[i])
        if item == 1:
            pass
        else:
            trigger = 0
            for m in range(item):
                if m > item/2:
                    break
                elif m!=1 and m != 0:
                    if item % m == 0:
                        trigger += 1

            if not trigger:
                cnt+=1

print(cnt)