# 백준 1541 잃어버린 괄호

import sys

equa = sys.stdin.readline().strip().split("-")
min_answer = 0

for i in range(len(equa)):
    if i == 0:
        if '+' in equa[i]:
            s_spl = map(int, equa[i].split("+"))
            min_answer += sum(s_spl)
        else:
            min_answer += int(equa[i])
    else:
        if '+' in equa[i]:
            s_spl = map(int, equa[i].split("+"))
            min_answer -= sum(s_spl)
        else:
            min_answer -= int(equa[i])

print(min_answer)