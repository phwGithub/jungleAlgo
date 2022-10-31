# 백준 1074 Z

cnt = 0
def z(n ,r, c):
    global cnt
    if n == 1:        
        if r < n and c < n:
            cnt += 0
            return
        if r < n and c >= n:
            cnt += 1
            return
        if r >= n and c < n:
            cnt += 2
            return
        if r >= n and c >= n:
            cnt += 3
            return

    half = (2 ** (n - 1))    
    if r < half and c < half:
        cnt += 0
        z(n - 1, r, c)
        return
    if r < half and c >= half:
        cnt += half * half * 1
        z(n - 1, r, c - half)
        return
    if r >= half and c < half:
        cnt += half * half * 2
        z(n - 1, r - half, c)
        return
    if r >= half and c >= half:
        cnt += half * half * 3
        z(n - 1, r - half, c - half)
        return


n, r, c = map(int, input().split(" "))

z(n, r, c)
print(cnt)