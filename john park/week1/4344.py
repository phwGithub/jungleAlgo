import sys

n = int(sys.stdin.readline())

for i in range(n):
    overAvg = 0
    
    testcase = list(map(int, sys.stdin.readline().split()))
    m = int(testcase[0])
    average = sum(testcase[1:])/m

    for j in testcase[1:]:
        if j>average:
            overAvg += 1

    percent = (overAvg/m)*100

    print( "%0.3f%%" % percent)
