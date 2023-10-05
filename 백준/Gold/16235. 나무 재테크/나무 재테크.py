n, m, k = map(int, input().split())
arr = [[5] * n for _ in range(n)]
s2d2 = [list(map(int, input().split())) for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
for i in range(n):
    for j in range(n):
        tree[i][j].sort()
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
while k > 0:
    new_tree = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nutrient = 0
            for age in tree[i][j]:
                if arr[i][j] >= age:
                    arr[i][j] -= age
                    new_tree[i][j].append(age + 1)
                    if (age + 1) % 5 == 0:
                        for di, dj in d:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                new_tree[ni][nj].append(1)
                else:
                    nutrient += age // 2
            arr[i][j] += nutrient
    tree = new_tree
    for i in range(n):
        for j in range(n):
            arr[i][j] += s2d2[i][j]
            tree[i][j].sort()
    k -= 1
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])
print(answer)