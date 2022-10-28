# 백준 2588 곱셈

num1 = input()
num2 = input()[::-1]

answer = 0
for idx, ch2 in enumerate(num2):
    print(int(num1) * int(ch2))
    answer += (int(num1) * int(ch2)) * int(pow(10, idx))

print(answer)