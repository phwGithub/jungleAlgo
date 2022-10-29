import sys

num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())
num3 = int(sys.stdin.readline())

result = num1 * num2 * num3
result = list(str(result))

for i in range(10):
    count = 0
    for j in result:
        if int(j) == i:
            count += 1
    print(count)
