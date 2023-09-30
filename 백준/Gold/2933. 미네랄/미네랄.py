from collections import deque
def down(a, b):
    cluster = [(a, b)]
    bottom_cluster = [-1] * c
    bottom_cluster[b] = a
    q = deque([(a, b)])
    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < r and 0 <= nj < c and cave[ni][nj] == 'x' and not checked[ni][nj]:
                cluster.append((ni, nj))
                q.append((ni, nj))
                checked[ni][nj] = True
                if bottom_cluster[nj] < ni:
                    bottom_cluster[nj] = ni
    down_cnt = 100
    for j in range(c):
        if bottom_cluster[j] > -1:
            for i in range(bottom_cluster[j] + 1, r):
                if cave[i][j] == 'x':
                    tmp = i - bottom_cluster[j] - 1
                    break
            else:
                tmp = r - bottom_cluster[j] - 1
            if tmp < down_cnt:
                down_cnt = tmp
    if down_cnt > 0:
        cluster.sort(reverse=True)
        for i, j in cluster:
            cave[i][j] = '.'
            cave[i+down_cnt][j] = 'x'
        return True
    return False


r, c = map(int, input().split())
cave = [list(input()) for _ in range(r)]
n = int(input())
stick = list(map(int, input().split()))
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for idx in range(n):
    for i in range(c):
        # 홀수(오른쪽에서 왼쪽으로 날아감)
        if idx % 2:
            if cave[r-stick[idx]][-i-1] == 'x':
                cave[r-stick[idx]][-i-1] = '.'
                break
        # 짝수(왼쪽에서 오른쪽으로 날아감)
        else:
            if cave[r-stick[idx]][i] == 'x':
                cave[r-stick[idx]][i] = '.'
                break
    else: continue
    checked = [[False] * c for _ in range(r)]
    flag = False
    for i in range(r):
        for j in range(c):
            if not checked[i][j] and cave[i][j] == 'x':
                checked[i][j] = True
                if down(i, j):
                    flag = True
                    break
        if flag:
            break
for i in range(r):
    print(''.join(cave[i]))