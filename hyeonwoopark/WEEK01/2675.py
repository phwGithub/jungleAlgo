# 백준 2675 문자열 반복

t = int(input())

for i in range(t):
    n , given_str = input().split(" ")

    for ch in given_str:
        for j in range(int(n)):
            print(ch,end="")

    print()