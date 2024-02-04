import sys
input = sys.stdin.readline
n = int(input())
check = [[0] * n for _ in range(n)]
numbers = input().split()
for i in range(n):
    check[i][i] = 1
    if i < n - 1 and numbers[i] == numbers[i+1]:
        check[i][i+1] = 1
for cnt in range(2, n+1):
    for i in range(n-1):
        if i + cnt > n - 1:
            break
        if check[i+1][i+cnt-1] and numbers[i] == numbers[i+cnt]:
            check[i][i+cnt] = 1
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(check[s-1][e-1])