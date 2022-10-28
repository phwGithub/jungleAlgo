# 백준 1978 소수 찾기

def findPrimeNumber(n : int):
    prime_list = [True] * (n + 1)
    prime_list[0] = False
    prime_list[1] = False

    for i in range(2, n):
        if(not prime_list[i]):
            continue
        
        j = 2
        while(i * j <= n):
            prime_list[i * j] = False
            j += 1
    
    return prime_list


n = int(input())
num_list = list(map(int, input().split(" ")))
prime_list = findPrimeNumber(1000)
prime_cnt = 0
for num in num_list:
    if(prime_list[num]):
        prime_cnt += 1

print(prime_cnt)
