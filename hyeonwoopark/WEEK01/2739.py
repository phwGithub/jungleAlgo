# 백준 2793 구구단

n = int(input())

for i in range(1, 10):
    print("{0} * {1} = {2}".format(n, i, n * i))