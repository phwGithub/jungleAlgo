# 백준 10872 팩토리얼

def factorial(n : int):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input())

print(factorial(n))