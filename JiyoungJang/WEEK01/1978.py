import sys
input = sys.stdin.readline

# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
# 주어진 수들 중 소수의 개수를 출력한다.

# 500까지의 모든 수로 나눠지는지 검사한다..? 숫자마다? 
# 소수 판별법? 
# 주어진 숫자를 반으로 나눈다음에 num/2까지 for문 돌리면서 검사한다 

## TODO : 추후 고칠 것!! 

n = int(input())
data = list(map(int, input().split())) # 판별할 숫자 list 
finalcount = 0

for numData in data : # numData = 판별할 숫자 
    keynum = int(numData/2)
    flag = 0
    for count in range(2, keynum) : # 2 부터 keynum 까지 나눠지는지 본다
        print(count, numData)
        if numData % count == 0 : 
            # 인수 있음, 소수 아님 
            break
        else : # 인수 없음, 소수
            finalcount += 1
            
    print(finalcount)
        
        # print()
print(finalcount)
    