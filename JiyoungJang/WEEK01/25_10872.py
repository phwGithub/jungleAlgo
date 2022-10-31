import sys
input = sys.stdin.readline

n = int(input())

def factorial (n : int) : 
    if n == 0 : 
        return 1
    return n * factorial(n - 1)

print(factorial(n))
