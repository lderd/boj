n = int(input())
arr = list(map(int, input().split()))
memo = [0] * n
for i in range(n):
    tmp = [0] * n
    for j in range(n):
        if j == 0:
            if arr[j] == arr[-i-1]:
                tmp[j] = 1
            else:
                tmp[j] = 0
        else:
            if arr[j] == arr[-i-1]:
                tmp[j] = max(tmp[j-1], memo[j-1] + 1)
            else:
                tmp[j] = max(tmp[j-1], memo[j])
    memo = tmp
print(n - memo[n-1])