import sys

n = int(sys.stdin.readline())

listW = [None] * 20000

for i in range(1,n+1):
    x = sys.stdin.readline().rstrip()
    if x not in listW:
        for j in range(i):
            if not listW[j]:
                listW[j] = x
                break
                
            elif len(x) < len(listW[j]):
                y = listW[j]
                listW[j] = x
                x = y

            elif len(x) == len(listW[j]):
                if x < listW[j]:
                    y = listW[j]
                    listW[j] = x
                    x = y





for i in listW:
    if i:
        print(i)
    else:
        break
