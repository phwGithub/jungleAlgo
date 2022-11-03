input_item = input("").split(" ")
x = int(input_item[0])
y = int(input_item[1])
w = int(input_item[2])
h = int(input_item[3])

condition1 = w-x
condition2 = h-y

list1 = [x,y,condition1,condition2]
list1.sort()
print(list1[0])
