item1=int(input(""))
item2=int(input(""))
item3=int(input(""))

lastItem = str(item1 * item2 * item3)

for i in range(10):
    print(lastItem.count(f"{i}"))