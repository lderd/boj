def solve(a, b):
    if a > b:
        return a
    mid = (a + b) // 2
    if 100 * (y + mid) // (x + mid) > z:
        return solve(a, mid - 1)
    else:
        return solve(mid + 1, b)


x, y = map(int, input().split())
z = 100 * y // x
if z >= 99:
    print(-1)
else:
    answer = solve(1, 10000000000)
    print(answer)