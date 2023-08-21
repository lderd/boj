def solve(a):
    if answer[a] > 0:
        return answer[a]
    elif len(before[a]) == 0:
        answer[a] = time[a]
        return answer[a]
    for b in before[a]:
        answer[a] = max(answer[a], solve(b) + time[a])
    return answer[a]


n = int(input())
before = [set() for _ in range(n)]
time = [0] * n
answer = [0] * n
for i in range(n):
    tmp = list(map(int, input().split()))
    time[i] = tmp[0]
    for j in range(1, len(tmp) - 1):
        before[i].add(tmp[j] - 1)
for i in range(n):
    print(solve(i))