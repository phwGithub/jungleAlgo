import sys

n = int(sys.stdin.readline())

for i in range(n):
    score = 0
    icmt = 1
    testcase = sys.stdin.readline()

    for j in range(len(testcase)):
        if j == 0 and testcase[0] == "O":
            score += icmt
            icmt += 1

        elif testcase[j] =="O":
            score += icmt
            icmt += 1
        
        elif testcase[j] == "X":
            icmt = 1
    print(score)
