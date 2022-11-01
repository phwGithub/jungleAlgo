import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**8)

# 하노이탑

# 기둥 이름을 1 2 3
# 1 -> 3 으로 n개 옮기는 방법은 
#     1. 1 -> 2로 n-1 개를 옮긴다 
#     2. 1 -> 3으로 마지막 원판을 옮긴다 
#     3. 2 -> 3으로 n-1개를 옮긴다 
# 따라서 입력값은 hanoi(n개, 기둥이름, 기둥이름)

n = int(input())

# n : 원판개수      first,last : 옮길 기둥 이름 
def hanoi(n : int, first : int, last : int) : 
    if n < 1 : return 0
    if n == 1 : 
        print(f'{first} {last}')
        return 0
    hanoi(n-1, first, 6 - (first + last))
    print(f'{first} {last}')
    hanoi(n-1, 6 - (first + last), last)
    return 0
        
print(2**n - 1)
if n <= 20 : 
    hanoi(n, 1, 3)
