n = int(input())
A = list(map(int, input().split()))
memo = [[A[0]]]
answer_len = 1
answer = [A[0]]
for i in range(1, n):
    tmp = []
    for j in range(i):
        if A[j] < A[i] and len(memo[j]) >= len(tmp):
            tmp = memo[j]
    memo.append(tmp + [A[i]])
    if answer_len < len(memo[-1]):
        answer_len = len(memo[-1])
        answer = memo[-1]
print(answer_len)
print(*answer)