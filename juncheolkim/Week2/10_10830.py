
DIV = 1000

def mul(A,B,n):
    rst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                rst[i][j] += (A[i][k] * B[k][j])
            rst[i][j] %= DIV
    return rst

def solve():
    n, b = [int(x) for x in input().split()]
    mat = []
    for _ in range(n):
        tmp = [int(x) for x in input().split()]
        mat.append(tmp)
    for i in range(n):
        for j in range(n):
            mat[i][j] %= DIV
    rst = [[0] * n for _ in range(n)]
    for i in range(n):
        rst[i][i] = 1
    while b != 0:
        if b % 2 == 1:
            rst = mul(rst, mat, n)
        mat = mul(mat, mat, n)
        b >>= 1
    for i in range(n):
        for j in range(n-1):
            print(rst[i][j], end=' ')
        print(rst[i][-1])
solve()
