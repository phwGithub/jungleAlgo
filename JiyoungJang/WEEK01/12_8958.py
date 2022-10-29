import sys
input = sys.stdin.readline

listNum = int(input())
# scoreList = []


for i in range(0, listNum):
    finalScore = 0
    xoString = input() # 'XXX0000'같은 str 
    scoreList = xoString.strip().split('X') # '000''00'str들을 모아놓은 리스트
    # print(scoreList)
    for oString in scoreList : # oString = 'ooo'같은 개별 str
        n = len(oString)
        # 총 점수는 n(0갯수)까지의 모든 자연수의 합
        finalScore += n*(n+1)/2
    print(int(finalScore))