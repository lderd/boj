N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = [0] * (N+1)
for i in range(N + 1):
    t = 0
    p = 0
    if i < N:
        t = arr[i][0]
        p = arr[i][1]
    if i >= 1:
        answer[i] = max(answer[i-1], answer[i])
    if i + t <= N:
        answer[i+t] = max(answer[i] + p, answer[i+t])
print(answer[N])