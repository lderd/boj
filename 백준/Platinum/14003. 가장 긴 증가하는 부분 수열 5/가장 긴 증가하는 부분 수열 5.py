def cus_bisect(x):
    left = 0
    right = answer_len - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[idx_memo[mid]] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


n = int(input())
arr = list(map(int, input().split()))
memo = [-1] * n

memo[0] = 0
idx_memo = [0]

answer_len = 1
answer_idx = 0
for i in range(1, n):
    idx = cus_bisect(arr[i])
    if idx == 0:
        memo[i] = i
        idx_memo[0] = i

    elif idx >= answer_len:
        memo[i] = idx_memo[idx - 1]
        idx_memo += [i]

        answer_len = idx + 1
        answer_idx = i

    else:
        memo[i] = idx_memo[idx - 1]
        idx_memo[idx] = i

print(answer_len)
answer = [arr[answer_idx]]
while memo[answer_idx] != answer_idx:
    answer.append(arr[memo[answer_idx]])
    answer_idx = memo[answer_idx]
print(*reversed(answer))