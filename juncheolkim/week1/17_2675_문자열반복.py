cntTest = int(input(""))

listX = []
for i in range(cntTest):
    inputItem = input("").split(" ")
    strRes = ''

    for n in range(len(inputItem[1])):
        strRes += inputItem[1][n]*int(inputItem[0])
    listX.append(strRes)

for i in range(len(listX)):
    print(listX[i])