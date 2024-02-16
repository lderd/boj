def init(start, end, index):
    if start == end:
        tree[index] = [arr[start], arr[start]]
        return tree[index]
    mid = (start + end) // 2
    a, b = init(start, mid, index * 2)
    c, d = init(mid+1, end, index * 2 + 1)
    tree[index] = [min(a, c), max(b, d)]
    return tree[index]


def solve(start, end, index, left, right):
    if left > end or right < start:
        return [1000000001, 0]
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    a, b = solve(start, mid, index * 2, left, right)
    c, d = solve(mid + 1, end, index * 2 + 1, left, right)
    return [min(a, c), max(b, d)]


n, m = map(int, input().split())
tree = [[0, 0] for _ in range(n * 4)]
arr = []
for _ in range(n):
    arr.append(int(input()))

init(0, n-1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(*solve(0, n-1, 1, a-1, b-1))