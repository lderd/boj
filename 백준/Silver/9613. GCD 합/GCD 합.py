from itertools import combinations
from math import gcd
t = int(input())
for _ in range(t):
    n, *numbers = map(int, input().split())
    answer = 0
    for a, b in combinations(numbers, 2):
        answer += gcd(a, b)
    print(answer)