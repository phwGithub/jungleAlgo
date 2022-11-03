xlist = []
for i in range(int(input(""))):
    xlist.append(int(input("")))

res = []
for m in range(len(xlist)):
    for n in range(int((xlist[m])/2)):
        x= int((xlist[m])/2) - n
        tog = False
        for i in range(2,x):
            if x % i == 0 :
                tog = True
        if tog == False :
            x2= xlist[m] - x
            tog2 = False
            for i in range(2,x2):
                if x2 % i == 0 :
                    tog2 = True
            if tog2 == False:
                res.append([x,x2])
                break

for i in res:
    print(str(i[0])+" "+str(i[1]))
