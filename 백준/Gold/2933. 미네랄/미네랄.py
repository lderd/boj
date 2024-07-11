r, c = map(int, input().split())
cave = [list(input()) for _ in range(r)]
n = int(input())
hs = list(map(int, input().split()))
for idx in range(n):
    h = hs[idx]
    bi = bj = -1
    # 홀수면 오른쪽에서 발사
    if idx % 2:
        for j in range(c-1, -1, -1):
            if cave[r-h][j] == 'x':
                bi, bj = r-h, j
                break
    # 짝수면 왼쪽에서 발사
    else:
        for j in range(c):
            if cave[r-h][j] == 'x':
                bi, bj = r-h, j
                break
    if bi == bj == -1: continue
    cave[bi][bj] = '.'
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    checked = set()
    for bdi, bdj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ci, cj = bi+bdi, bj+bdj
        # 깨진 미네랄 주변에 미네랄이 있다면 해당 클러스터는 공중에 뜨게 될 가능성이 있다
        if 0 <= ci < r and 0 <= cj < c and (ci, cj) not in checked and cave[ci][cj] == 'x':
            checked.add((ci, cj))
            cluster = {(ci, cj)}
            down = True
            q = [(ci, cj)]
            while q:
                i, j = q.pop()
                for di, dj in d:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < r and 0 <= nj < c and cave[ni][nj] == 'x' and (ni, nj) not in cluster:
                        q.append((ni, nj))
                        if ni == r - 1:
                            down = False
                        cluster.add((ni, nj))
                        if (ni == bi - 1 and nj == bj) or (ni == bi + 1 and nj == bj) or (ni == bi and nj == bj - 1) or (ni == bi and nj == bj + 1):
                            checked.add((ni, nj))
            flag = False
            while down:
                cluster_list = sorted(cluster, reverse=True)
                new_cluster = set()
                for i, j in cluster_list:
                    new_cluster.add((i+1, j))
                    cave[i+1][j] = 'x'
                    cave[i][j] = '.'
                    if i + 1 == r - 1 or ((i + 1, j) not in cluster and cave[i+2][j] == 'x'):
                        down = False
                        flag = True
                cluster = new_cluster
            # 클러스터는 한번에 하나만 떨어진다
            if flag:
                break
for i in range(r):
    print(''.join(cave[i]))