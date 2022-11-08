import sys
from bisect import bisect_left
input = sys.stdin.readline

m, n, l = map(int, input().split())
shoot = list(map(int, input().split()))
shoot.sort()

cnt = 0
for _ in range(n):
    x, y = map(int, input().split()) # 동물을 입력하는 순간 바로 계산
    if y <= l:
        idx = bisect_left(shoot, x) # 배열 이진 분할 알고리즘
        for k in [idx-1, idx, idx+1]:
            if k < 0 or k >= m:
                continue
            if abs(shoot[k] - x) + y <= l:
                cnt += 1
                break
print(cnt)