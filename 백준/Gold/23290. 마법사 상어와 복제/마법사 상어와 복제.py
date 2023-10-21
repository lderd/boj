# 물고기, 연습 수
m, s = map(int, input().split())
arr = [[[0] * 8 for _ in range(4)] for _ in range(4)]
for _ in range(m):
    x, y, d = map(int, input().split())
    arr[x-1][y-1][d-1] += 1
fish_d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark_i, shark_j = map(lambda x:int(x)-1, input().split())
shark_d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
smell_one = set()
smell_two = set()
for _ in range(s):
    new_arr = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for d in range(8):
                if arr[i][j][d] == 0: continue
                fi, fj, fd = int(), int(), int()
                for cnt in range(8):
                    fd = (d + cnt * 7) % 8
                    fdi, fdj = fish_d[fd]
                    nfi, nfj = i + fdi, j + fdj
                    if 0 <= nfi < 4 and 0 <= nfj < 4 and not (nfi == shark_i and nfj == shark_j) and (nfi, nfj) not in smell_one and (nfi, nfj) not in smell_two:
                        fi, fj = nfi, nfj
                        break
                else:
                    fi, fj, fd = i, j, d
                new_arr[fi][fj][fd] += arr[i][j][d]
    shark_q = [('', shark_i, shark_j, 0, set())]
    for _ in range(3):
        shark_nq = []
        for moving, si, sj, eaten, checked in shark_q:
            for d in range(4):
                di, dj = shark_d[d]
                ni, nj = si+di, sj+dj
                if 0 <= ni < 4 and 0 <= nj < 4:
                    if (ni, nj) not in checked:
                        shark_nq.append((moving + str(d), ni, nj, eaten + sum(new_arr[ni][nj]), checked | {(ni, nj)}))
                    else:
                        shark_nq.append((moving + str(d), ni, nj, eaten, checked | {(ni, nj)}))
        shark_q = shark_nq
    shark_q.sort(key=lambda x: [-x[3], x[0]])
    moving, shark_i, shark_j, eaten, checked = shark_q[0]
    smell_two = smell_one
    smell_one = set()
    for smell_i, smell_j in checked:
        for d in range(8):
            if new_arr[smell_i][smell_j][d] > 0:
                new_arr[smell_i][smell_j][d] = 0
                smell_one.add((smell_i, smell_j))
    for i in range(4):
        for j in range(4):
            for d in range(8):
                arr[i][j][d] += new_arr[i][j][d]
answer = 0
for i in range(4):
    for j in range(4):
        for d in range(8):
            answer += arr[i][j][d]
print(answer)