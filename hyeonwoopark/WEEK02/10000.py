# 백준 10000 원 영역

import sys

n = int(sys.stdin.readline())
circle_point_list = []
sections = 1

for i in range(n):
    x, r = map(int, sys.stdin.readline().strip().split(" "))

    circle_point_list.append(['(', x - r, 0, 0])
    circle_point_list.append([')', x + r, 0, 0])

circle_point_list.sort(key= lambda x: (x[1], -ord(x[0])))
stack = []

for circle_point in circle_point_list:
    #print(stack)
    if circle_point[0] == "(":
        if len(stack) != 0:
            if stack[-1][1] == circle_point[1] or stack[-1][3] == circle_point[1]:
                stack[-1][2] = 1
            else:
                stack[-1][2] = 0
            
        stack.append([circle_point[0], circle_point[1], 0, 0])
    
    else:
        top = stack.pop()
        if len(stack) > 0 and stack[-1][2] == 1:
            stack[-1][3] = circle_point[1]
        
        if top[2] == 1 and top[3] == circle_point[1]:
            sections += 1
        
        sections += 1
       
print(sections)


