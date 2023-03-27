from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
memo = [arr[0]]
answer = 1
for i in range(1, n):
    idx = bisect_left(memo, arr[i])
    if idx >= answer:
        memo.append(arr[i])
        answer += 1
    else:
        memo[idx] = arr[i]
print(answer)