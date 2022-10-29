import sys
input = sys.stdin.readline

# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

grade = int(input())

if grade < 60: 
    print('F')
elif grade < 70:
    print('D')
elif grade <80:
    print('C')
elif grade < 90:
    print('B')
else : print('A')
