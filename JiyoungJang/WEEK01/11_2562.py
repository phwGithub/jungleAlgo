import sys
input = sys.stdin.readline


nums = []
count = 0
temp = 0
for i in range(0, 9): 
    nums.append(int(input()))
    if i != 0 : 
        if nums[i] > temp : 
            temp = nums[i]
            count = i 
    else : temp = nums[i]
print(temp)
print(count + 1)