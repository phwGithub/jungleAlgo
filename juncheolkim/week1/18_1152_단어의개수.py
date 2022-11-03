item = input("")
item = item.split(" ")

listX = []
for i in range(len(item)):
    if not item[i] == "":
        listX.append(item[i])


print(len(listX))