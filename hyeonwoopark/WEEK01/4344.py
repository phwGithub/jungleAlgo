# 백준 4344 평균은 넘겠지

t = int(input())

def getAverage(scores : list):
    return sum(scores) / len(scores)

for i in range(t):
    scores = list(map(int, input().split(" ")))

    average = getAverage(scores[1:])
    pass_cnt = 0
    for score in scores[1:]:
        if(score > average):
            pass_cnt += 1
    
    answer = (pass_cnt / scores[0]) * 100
    print("{0:0.3f}%".format(answer))    
    