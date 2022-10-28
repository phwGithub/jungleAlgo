# 백준 10950 A + B - 3

t = int(input())
a = 0
b = 0

for i in range(t):
    a , b = map(int, input().split(" "))
    print(a + b)