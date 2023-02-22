from collections import defaultdict


def solve(i):
    if i == 0:
        return 0
    if memo[i]:
        return memo[i]
    memo[i] = (solve((i - 1) // 2) * solve(i // 2) + solve((i + 1) // 2) * solve((i + 2) // 2)) % 1000000007
    return memo[i]


n = int(input())
memo = defaultdict(int)
memo[0] = 0
memo[1] = 1
memo[2] = 1
print(solve(n))