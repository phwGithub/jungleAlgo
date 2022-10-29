# 백준 8958 OX퀴즈

t = int(input())

for i in range(t):
    quizResult = input()

    totalScore = 0
    seq = 0
    for answer in quizResult:
        if(answer == "X"):
            seq = 0
            continue

        if(answer == "O"):
            seq += 1
            totalScore += seq
            continue

    print(totalScore)