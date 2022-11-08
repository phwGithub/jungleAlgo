import sys


A , B , C = list(map(int, sys.stdin.readline().rstrip().split(' '))) # ( A**B ) % C 를 구하여라

# 지수 법칙 : A**(m + n) = A**m * A**n
# 나머지 분배 법칙 : (A*B) % C = (A%C) * (B%C) % C

def multi (a,b):
  if b == 1:
      return a%C
  else:
      tmp = multi(a,b//2)
      if b % 2 ==0:
          return (tmp * tmp) % C
      else:
          return (tmp  * tmp *a) % C
          
print(multi(A,B))