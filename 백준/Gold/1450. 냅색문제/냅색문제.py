from itertools import combinations
from bisect import bisect_right
n, c = map(int, input().split())
prise = list(map(int, input().split()))
a = prise[:n//2]
b = prise[n//2:]
a_sum = [0]
b_sum = [0]
for i in range(1, n//2 + 1):
    a_sum.extend(map(sum, combinations(a, i)))
for i in range(1, n + 1 - n//2):
    b_sum.extend(map(sum, combinations(b, i)))
a_sum.sort()
b_sum.sort()
answer = 0
for i in a_sum:
    answer += bisect_right(b_sum, c-i)
print(answer)