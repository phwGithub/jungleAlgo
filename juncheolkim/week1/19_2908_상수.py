item = input("")
item = item.split(" ")

item1 = int("".join(reversed(item[0])))
item2 = int("".join(reversed(item[1])))
listX = sorted([item1,item2])
print(listX[-1])