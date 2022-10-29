# 백준 2628 종이자르기

x_list = []
y_list = []

y_len, x_len = map(int, input().split(" "))

x_list.append(0)
y_list.append(0)
x_list.append(x_len)
y_list.append(y_len)

t = int(input())

for i in range(t):
    a, b = map(int, input().split(" "))

    if a == 0:
        x_list.append(b)
        continue

    if a == 1:
        y_list.append(b)
        continue

x_list.sort()
y_list.sort()

x_diff_list = []
y_diff_list = []

for i in range(len(x_list) - 1):
    x_diff_list.append(x_list[i + 1] - x_list[i])

for i in range(len(y_list) - 1):
    y_diff_list.append(y_list[i + 1] - y_list[i])


print(max(x_diff_list) * max(y_diff_list))
