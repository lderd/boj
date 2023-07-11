def solve(min_, max_, ssum, index):
    global answer
    if ssum > r:
        return
    if index >= n:
        if max_ - min_ >= x and l <= ssum:
            answer += 1
        return
    if min_ == 0:
        solve(A[index], A[index], A[index], index + 1)
        solve(0, 0, 0, index + 1)
    else:
        solve(min_, A[index], ssum + A[index], index + 1)
        solve(min_, max_, ssum, index + 1)


n, l, r, x = map(int, input().split())
A = sorted(list(map(int, input().split())))
answer = 0
solve(0, 0, 0, 0)
print(answer)