# 백준 2110 공유기 설치

import sys

n, c = map(int, sys.stdin.readline().strip().split(" "))
num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list = sorted(num_list)
ans = sys.maxsize * -1

if c == 2:
    print(num_list[-1] - num_list[0])

else:
    st = 1
    ed = num_list[-1] - num_list[0]

    while st <= ed:
        mid = (st + ed) // 2

        cnt = 1
        cur_pos = num_list[0]
        for i in range(1, n):
            if cur_pos + mid <= num_list[i]:
                cnt += 1
                cur_pos = num_list[i]
    
        if cnt >= c:
            ans = max(ans, mid)
            st = mid + 1
        else:
            ed = mid - 1

    print(ans)