import sys
list = []
for _ in range(9):
    x = int(input())
    list.append(x)

print(max(list))
print(list.index(max(list))+1)
