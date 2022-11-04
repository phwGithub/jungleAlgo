listX = []
for i in range(9):
    listX.append(int(input("")))

listY = sorted(listX)
apex = listY[-1]
indexItem = listX.index(apex)
print(apex)
print(indexItem+1)