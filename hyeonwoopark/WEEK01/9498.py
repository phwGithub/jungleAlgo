# 백준 9498 시험성적

def getGrade(score : int):
    if(score >= 90 and score <= 100):
        return "A"

    if(score >= 80 and score <= 89):
        return "B"

    if(score >= 70 and score <= 79):
        return "C"

    if(score >= 60 and score <= 69):
        return "D"

    return "F"

score = int(input())

print(getGrade(score))

