item = input("")
item = item.split(" ")

item1 = int(item[0])
item2 = int(item[1])
item3 = int(item[2])

itemKEY = item1 - item2
totalDis = item3 - item2
if totalDis % itemKEY == 0:
    res = totalDis // itemKEY
else:
    
    res = totalDis // itemKEY + 1

print(res)