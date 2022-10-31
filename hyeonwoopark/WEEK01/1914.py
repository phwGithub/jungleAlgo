# 백준 1914 하노이의 탑

def hanoi(n : int, fr : str, to : str):
    if n == 0:
        return

    if n == 1:
        print("{0} {1}".format(fr, to))
        return

    hanoi(n - 1, fr, str(6 - int(fr) - int(to)))
    hanoi(1, fr, to)
    hanoi(n - 1, str(6 - int(fr) - int(to)), to)


n = int(input())

print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3)