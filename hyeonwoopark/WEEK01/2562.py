# 백준 2562 최댓값

num_list = []

for i in range(9):
    num_list.append(int(input()))

max = -1
idx = -1

for index, num in enumerate(num_list):
    if(num > max):
        max = num
        idx = index

print(max)
print(idx + 1)