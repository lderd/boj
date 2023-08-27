def solve(idx, cnt, checked):
    if cnt > answer[idx % 2]:
        answer[idx % 2] = cnt
    if idx >= 2 * n - 1:
        return
    for j in arr1[idx]:
        if j not in checked:
            solve(idx + 2, cnt + 1, checked | {j})
    solve(idx + 2, cnt, checked)


n = int(input())
arr = [input().split() for _ in range(n)]
arr1 = [[] for _ in range(2 * n - 1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            arr1[i+j].append(n-1+j-i)
answer = [0, 0]
solve(0, 0, set())
solve(1, 0, set())
print(sum(answer))