testCnt = int(input(""))

printRes = []
for i in range(testCnt):
    
    inputX = input("").split(" ")
    cnt = int(inputX[0])
    total = 0
    for m in range(cnt):
        total += int(inputX[m+1])
    aver = total / cnt

    cntProud = 0
    for m in range(cnt):
        if int(inputX[m+1]) > aver :
            cntProud += 1
    
    lastPrint = cntProud / cnt
    printRes.append(round(lastPrint*100,3))

for i in range(testCnt):
    print(f"{printRes[i]:.3f}%")