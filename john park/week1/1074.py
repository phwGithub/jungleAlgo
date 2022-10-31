import sys
N, r, c = map(int, sys.stdin.readline().split())
# 1<= N <= 15

# 2^N * 2^N 인 2차원 배열

# 0 <= r, c < 2^N, r행 c열을 몇 번째로 방문했는지 출력
tempR = r
tempC = c
count = 0

for i in reversed(range(0, N+1)):
    if i == 0:
        if tempR == 0 and tempC == 0:
            break
        elif tempR == 0 and tempC == 1:
            count += 1
            break
        elif tempR == 1 and tempC == 0:
            count += 2
            break
        elif tempR == 1 and tempC == 1:
            count += 3
            break
    if tempR < 2**(i-1) and tempC < 2**(i-1):
        pass
    elif tempR < 2**(i-1) and tempC >= 2**(i-1):
        count += 2**(2*i-2)
        tempC -= 2**(i-1)
    elif tempR >= 2**(i-1) and tempC < 2**(i-1):
        count += 2**(2*i-1)
        tempR -= 2**(i-1)
    elif tempR >= 2**(i-1) and tempC >= 2**(i-1):
        count += 3*(2**(2*i-2))
        tempR -= 2**(i-1)
        tempC -= 2**(i-1)

print(count)
