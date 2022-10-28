# 백준 2577 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

mul = a * b * c

digits = [0 for i in range(10)]

for digit in str(mul):
    digits[int(digit)] += 1

for digit in digits:
    print(digit)