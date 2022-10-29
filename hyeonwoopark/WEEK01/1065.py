# 백준 1065 한수

n = int(input())

hansu_cnt = 0
for i in range(1, n + 1):
    str_i = str(i)

    if len(str_i) == 1:
        hansu_cnt += 1
        continue
    
    diff = -1
    isHansu = True
    for j in range(len(str_i) - 1):
        if j == 0:
            diff = int(str_i[j + 1]) - int(str_i[j])
            continue

        if diff != int(str_i[j + 1]) - int(str_i[j]):
            isHansu = False
        
    if isHansu:
        hansu_cnt += 1

print(hansu_cnt)
