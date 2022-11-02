# 백준 2577 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

mul = a * b * c

digit_list = list(str(mul))

for i in range(10):
    print(digit_list.count(str(i)))