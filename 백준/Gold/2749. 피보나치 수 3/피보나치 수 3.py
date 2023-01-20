'''
f10 = f9 + f8
= f7 + 2f8
= 2f6 + 3f7
= 3f5 + 5f6
= ...
=>
f10 = f1*f8 + f1*f9
= f2*f7 + f3*f8
= f3*f6 + f4*f7
= f4*f5 + f5+f6
= f5*f4 + f6*f5


f11 = 1 9  2 10
= 2 8  3 9
= 3 7  4 8
= 4 6  5 7
= 5 5  6 6

f[n] = f[n//2] * f[(n-1)//2)] + f[(n+1)//2] * f[(n+2)//2]
'''
from collections import defaultdict


def solve(i):
    if i == 0:
        return 0
    if memo[i]:
        return memo[i]
    memo[i] = (solve((i - 1) // 2) * solve(i // 2) + solve((i + 1) // 2) * solve((i + 2) // 2)) % 1000000
    return memo[i]


n = int(input())
memo = defaultdict(int)
memo[0] = 0
memo[1] = 1
memo[2] = 1
print(solve(n))
