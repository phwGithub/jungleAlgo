import sys
input = sys.stdin.readline

C = int(input())

for lines in range(0, C):
    scoreList = list(map(int, input().split())) # 학생 수까지 포함한 점수 리스트 
    gradeSum = sum(scoreList[1:])
    gradeAvg = gradeSum / scoreList[0]
    abovAvg = 0
    for students in scoreList[1:] : 
        if students > gradeAvg : 
            abovAvg += 1    # 평균 이상인 학생 수 
    # print(round(abovAvg / scoreList[0] * 100, 3),'%') 
    # 정답이 아님??? %를 떼서 출력해서 그런가? 
    rate = abovAvg / scoreList[0] * 100
    print(f'{rate:.3f}%')
    
    
    
            