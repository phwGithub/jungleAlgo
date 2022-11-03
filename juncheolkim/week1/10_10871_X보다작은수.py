input_item1 = input("")
item1 = int(input_item1.split(" ")[0])
item2 = int(input_item1.split(" ")[1])

input_item2 = input("")
for i in range(item1):
    globals()[f'item2_{i}'] = int(input_item2.split(" ")[i])

listX = []
for i in range(item1):
    item3 = eval(f'item2_{i}')
    if item2 > item3:
        listX.append(item3)

strX = ''
for i in range(len(listX)):
    if not i == len(listX) -1 :
        strX += str(listX[i]) + " "
    else:
        strX += str(listX[i])

print(strX)