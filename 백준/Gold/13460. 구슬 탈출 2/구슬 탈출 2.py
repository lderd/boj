from collections import deque
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
checked = [[[[False] * (m - 2) for _ in range(n - 2)] for _ in range(m - 2)] for _ in range(n - 2)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            ri = i
            rj = j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bi = i
            bj = j
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            O = (i, j)
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque([(ri, rj, bi, bj, 0)])
checked[ri-1][rj-1][bi-1][bj-1] = True
answer = -1
rgo = True
bgo = True
while q:
    ri, rj, bi, bj, cnt = q.popleft()
    nri = nrj = nbi = nbj = int()
    if cnt >= 10:
        break
    for d in range(4):
        rgo = True
        bgo = True
        if d == 0:
            # 빨간거 먼저 이동
            if ri < bi:
                c = 1
                while True:
                    nri = ri + direction[d][0] * c
                    nrj = rj + direction[d][1] * c
                    if 1 <= nri < n - 1 and 1 <= nrj < m - 1:
                        if arr[nri][nrj] == 'O':
                            answer = cnt + 1
                            rgo = False
                            c += 1
                            break
                        elif arr[nri][nrj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nri = ri + direction[d][0] * c
                nrj = rj + direction[d][1] * c
                c = 1
                while True:
                    nbi = bi + direction[d][0] * c
                    nbj = bj + direction[d][1] * c
                    if 1 <= nbi < n - 1 and 1 <= nbj < m - 1 and (nbi, nbj) != (nri, nrj):
                        if arr[nbi][nbj] == 'O':
                            bgo = False
                            break
                        elif arr[nbi][nbj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nbi = bi + direction[d][0] * c
                nbj = bj + direction[d][1] * c
            else:
                c = 1
                while True:
                    nbi = bi + direction[d][0] * c
                    nbj = bj + direction[d][1] * c
                    if 1 <= nbi < n - 1 and 1 <= nbj < m - 1:
                        if arr[nbi][nbj] == 'O':
                            bgo = False
                            break
                        elif arr[nbi][nbj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nbi = bi + direction[d][0] * c
                nbj = bj + direction[d][1] * c
                c = 1
                while True:
                    nri = ri + direction[d][0] * c
                    nrj = rj + direction[d][1] * c
                    if 1 <= nri < n - 1 and 1 <= nrj < m - 1 and (nbi, nbj) != (nri, nrj):
                        if arr[nri][nrj] == 'O':
                            answer = cnt + 1
                            rgo = False
                            break
                        elif arr[nri][nrj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nri = ri + direction[d][0] * c
                nrj = rj + direction[d][1] * c
        elif d == 1:
            if ri > bi:
                c = 1
                while True:
                    nri = ri + direction[d][0] * c
                    nrj = rj + direction[d][1] * c
                    if 1 <= nri < n - 1 and 1 <= nrj < m - 1:
                        if arr[nri][nrj] == 'O':
                            answer = cnt + 1
                            rgo = False
                            c += 1
                            break
                        elif arr[nri][nrj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nri = ri + direction[d][0] * c
                nrj = rj + direction[d][1] * c
                c = 1
                while True:
                    nbi = bi + direction[d][0] * c
                    nbj = bj + direction[d][1] * c
                    if 1 <= nbi < n - 1 and 1 <= nbj < m - 1 and (nbi, nbj) != (nri, nrj):
                        if arr[nbi][nbj] == 'O':
                            bgo = False
                            break
                        elif arr[nbi][nbj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nbi = bi + direction[d][0] * c
                nbj = bj + direction[d][1] * c
            else:
                c = 1
                while True:
                    nbi = bi + direction[d][0] * c
                    nbj = bj + direction[d][1] * c
                    if 1 <= nbi < n - 1 and 1 <= nbj < m - 1:
                        if arr[nbi][nbj] == 'O':
                            bgo = False
                            break
                        elif arr[nbi][nbj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nbi = bi + direction[d][0] * c
                nbj = bj + direction[d][1] * c
                c = 1
                while True:
                    nri = ri + direction[d][0] * c
                    nrj = rj + direction[d][1] * c
                    if 1 <= nri < n - 1 and 1 <= nrj < m - 1 and (nbi, nbj) != (nri, nrj):
                        if arr[nri][nrj] == 'O':
                            answer = cnt + 1
                            rgo = False
                            break
                        elif arr[nri][nrj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nri = ri + direction[d][0] * c
                nrj = rj + direction[d][1] * c
        elif d == 2:
            if rj < bj:
                c = 1
                while True:
                    nri = ri + direction[d][0] * c
                    nrj = rj + direction[d][1] * c
                    if 1 <= nri < n - 1 and 1 <= nrj < m - 1:
                        if arr[nri][nrj] == 'O':
                            answer = cnt + 1
                            rgo = False
                            c += 1
                            break
                        elif arr[nri][nrj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nri = ri + direction[d][0] * c
                nrj = rj + direction[d][1] * c
                c = 1
                while True:
                    nbi = bi + direction[d][0] * c
                    nbj = bj + direction[d][1] * c
                    if 1 <= nbi < n - 1 and 1 <= nbj < m - 1 and (nbi, nbj) != (nri, nrj):
                        if arr[nbi][nbj] == 'O':
                            bgo = False
                            break
                        elif arr[nbi][nbj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nbi = bi + direction[d][0] * c
                nbj = bj + direction[d][1] * c
            else:
                c = 1
                while True:
                    nbi = bi + direction[d][0] * c
                    nbj = bj + direction[d][1] * c
                    if 1 <= nbi < n - 1 and 1 <= nbj < m - 1:
                        if arr[nbi][nbj] == 'O':
                            bgo = False
                            break
                        elif arr[nbi][nbj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nbi = bi + direction[d][0] * c
                nbj = bj + direction[d][1] * c
                c = 1
                while True:
                    nri = ri + direction[d][0] * c
                    nrj = rj + direction[d][1] * c
                    if 1 <= nri < n - 1 and 1 <= nrj < m - 1 and (nbi, nbj) != (nri, nrj):
                        if arr[nri][nrj] == 'O':
                            answer = cnt + 1
                            rgo = False
                            break
                        elif arr[nri][nrj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nri = ri + direction[d][0] * c
                nrj = rj + direction[d][1] * c
        elif d == 3:
            if rj > bj:
                c = 1
                while True:
                    nri = ri + direction[d][0] * c
                    nrj = rj + direction[d][1] * c
                    if 1 <= nri < n - 1 and 1 <= nrj < m - 1:
                        if arr[nri][nrj] == 'O':
                            answer = cnt + 1
                            rgo = False
                            c += 1
                            break
                        elif arr[nri][nrj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nri = ri + direction[d][0] * c
                nrj = rj + direction[d][1] * c
                c = 1
                while True:
                    nbi = bi + direction[d][0] * c
                    nbj = bj + direction[d][1] * c
                    if 1 <= nbi < n - 1 and 1 <= nbj < m - 1 and (nbi, nbj) != (nri, nrj):
                        if arr[nbi][nbj] == 'O':
                            bgo = False
                            break
                        elif arr[nbi][nbj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nbi = bi + direction[d][0] * c
                nbj = bj + direction[d][1] * c
            else:
                c = 1
                while True:
                    nbi = bi + direction[d][0] * c
                    nbj = bj + direction[d][1] * c
                    if 1 <= nbi < n - 1 and 1 <= nbj < m - 1:
                        if arr[nbi][nbj] == 'O':
                            bgo = False
                            break
                        elif arr[nbi][nbj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nbi = bi + direction[d][0] * c
                nbj = bj + direction[d][1] * c
                c = 1
                while True:
                    nri = ri + direction[d][0] * c
                    nrj = rj + direction[d][1] * c
                    if 1 <= nri < n - 1 and 1 <= nrj < m - 1 and (nbi, nbj) != (nri, nrj):
                        if arr[nri][nrj] == 'O':
                            answer = cnt + 1
                            rgo = False
                            break
                        elif arr[nri][nrj] == '.':
                            c += 1
                        else:
                            c -= 1
                            break
                    else:
                        c -= 1
                        break
                nri = ri + direction[d][0] * c
                nrj = rj + direction[d][1] * c
        if rgo and bgo:
            if not checked[nri - 1][nrj - 1][nbi - 1][nbj - 1]:
                checked[nri - 1][nrj - 1][nbi - 1][nbj - 1] = True
                q.append((nri, nrj, nbi, nbj, cnt + 1))
        elif not rgo and bgo:
            break
        elif not bgo:
            answer = -1
    if not rgo and bgo:
        break
print(answer)