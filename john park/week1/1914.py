import sys

def hanoi(N : int):
    prevList=[]
    mainList=[1,3]
    nextList=[]

    resultList = []
    
    if N == 1:
        resultList.append(mainList)
        return resultList # [[1, 3]]
    
    # tempList = hanoi(N-1) # [[1,2][1,3][2,3]...]
    prevList=hanoi(N-1)
    for i in prevList: #[1,2], [1,3], [2,3], ...
        if (2 in i) and (3 in i):
            i[0], i[1] = i[1], i[0]
        elif 2 in i:
            idx = i.index(2)
            i[idx] = 3
        elif 3 in i:
            idx = i.index(3)
            i[idx] = 2
    

    # nextList=tempList
    nextList = hanoi(N-1)
    for j in nextList:
        if (1 in j) and (2 in j):
            j[0], j[1] = j[1], j[0]
        elif 1 in j:
            idx = j.index(1)
            j[idx] = 2
        elif 2 in j:
            idx = j.index(2)
            j[idx] = 1

    
    resultList += prevList
    resultList.append(mainList)
    resultList += nextList
    return resultList


K = int(sys.stdin.readline())
if K >20:
    print(2**K -1)
else:
    list1 = hanoi(K)
    print(len(list1))
    for l in list1:
        print( l[0], l[1] )
