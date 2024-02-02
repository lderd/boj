import sys
input = sys.stdin.readline
t = int(input())
memo = [0, 1, 1, 1, 2]
l = 4
for _ in range(t):
    n = int(input())
    if n > l:
        for i in range(l, n):
            memo.append(memo[i]+memo[i-4])
        l = n
    print(memo[n])
