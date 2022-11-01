import sys
N, k, p = map(int, sys.stdin.readline().split())

temp_count = 0
def z_function(n, r, c : int):
    global temp_count
    if n == 1:
        if r == 0 and c == 0:
            return
        elif r==0 and c==1:
            temp_count+=1
            return
        elif r==1 and c==0:
            temp_count+=2
            return
        elif r==1 and c==1:
            temp_count+=3
            return
    if r < 2**(n-1) and c < 2**(n-1): # n=2이면, r<2 and c<2
        z_function(n-1, r, c)
    elif r < 2**(n-1) and c >= 2**(n-1):
        temp_count += 2**(2*n-2)
        z_function(n-1, r, c-2**(n-1))
    elif r >= 2**(n-1) and c < 2**(n-1):
        temp_count += 2**(2*n-1)
        z_function(n-1, r-2**(n-1), c)
    elif r >= 2**(n-1) and c >= 2**(n-1):
        temp_count += 3*(2**(2*n-2))
        z_function(n-1, r-2**(n-1), c-2**(n-1))

z_function(N, k, p)

print(temp_count)
