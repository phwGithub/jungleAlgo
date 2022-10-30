import sys
import math

def eratosthenes(n:int):
    prime_list = [True for i in range (n+1)]
    prime_list[0] = False
    prime_list[1] = False
    
    for j in range(2, int(math.sqrt(n))+1):
        i = 2
        while j*i <= n:
            prime_list[j*i] = False
            i+=1
    return prime_list

prime_list = eratosthenes(10000)

T = int(sys.stdin.readline())

for _ in range(T):
    test_num = int(sys.stdin.readline())
    prime1 = 0
    prime2 = 0
    for i in range(2, int(test_num/2)+1):
        if i ==2 or i%2 ==1:
            if prime_list[i]:
                if prime_list[test_num-i]:
                    prime1 = i
                    prime2 = test_num-i
    print(prime1, prime2)
