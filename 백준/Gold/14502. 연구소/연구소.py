from itertools import combinations
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
binkan = set()
birus = set()
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            binkan.add((i, j))
        elif lab[i][j] == 2:
            birus.add((i, j))
answer = 0
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for combi in combinations(binkan, 3):
    checked = set(combi)
    for i, j in birus:
        q = [(i, j)]
        while q:
            ci, cj = q.pop()
            for di, dj in d:
                ni, nj = ci+di, cj+dj
                if 0 <= ni < n and 0 <= nj < m and lab[ni][nj] == 0 and (ni, nj) not in checked:
                    checked.add((ni, nj))
                    q.append((ni, nj))
    tmp = len(binkan) - len(checked)
    if answer < tmp:
        answer = tmp
print(answer)