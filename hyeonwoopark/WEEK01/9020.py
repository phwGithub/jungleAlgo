# 백준 9020 골드바흐 추측

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

t = int(input())
prime_list = findPrimeNumber(10000)

small_prime = -1
big_prime = -1
for i in range(t):
    some_even = int(input())

    for i in range(2, int(some_even / 2) + 1):
        if(prime_list[i] and prime_list[some_even - i]):
            small_prime = i
            big_prime = some_even - i
    
    print(small_prime, big_prime)