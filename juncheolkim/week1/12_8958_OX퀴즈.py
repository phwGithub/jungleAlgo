cntTest = int(input(""))

listX = []

for i in range(cntTest):
    cnt = 0
    score = 0

    x = input("")
    for m in range(len(x)):
        if x[m] == "O":
            cnt += 1
            score += cnt
        else:
            cnt = 0

    listX.append(score)

for i in range(cntTest):
    print(listX[i])