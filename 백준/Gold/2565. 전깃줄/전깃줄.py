from bisect import bisect_left
n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()
memo = [arr[0][1]]
for i in range(1, n):
    if memo[-1] < arr[i][1]:
        memo.append(arr[i][1])
    else:
        index = bisect_left(memo, arr[i][1])
        memo[index] = arr[i][1]
print(n - len(memo))