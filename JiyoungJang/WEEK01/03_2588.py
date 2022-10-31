import sys
input = sys.stdin.readline

num1 = int(input())
num2 = int(input())

n_1 = int(num2 % 10)    
n_2 = int(int(num2 % 100) / 10)
n_3 = int(num2 / 100)

print(num1 * n_1)
print(num1 * n_2)
print(num1 * n_3)

print(num1 * num2)