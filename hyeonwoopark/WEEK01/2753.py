# 백준 2753 윤년

def checkYun(year : int):
    if(year % 400 == 0):
        return True

    if(year % 4 == 0 and year % 100 != 0):
        return True

    return False

year = int(input())

if(checkYun(year)):
    print(1)
else:
    print(0)
