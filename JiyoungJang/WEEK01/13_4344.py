import sys
input = sys.stdin.readline

C = int(input())

for lines in range(0, C):
    scoreList = list(map(int, input().split()))
    gradeSum = sum(scoreList[1:])
    gradeAvg = gradeSum / scoreList[0]
    abovAvg = 0
    for students in scoreList[1:] : 
        if students > gradeAvg : 
            abovAvg += 1
    print(round(abovAvg / scoreList[0] * 100, 3),'%')
    
    
    
            