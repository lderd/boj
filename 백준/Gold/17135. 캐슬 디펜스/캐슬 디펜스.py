from itertools import combinations
from copy import deepcopy
from collections import deque
n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
hubos = list(combinations(list(range(m)), 3))
dlt = [(0, -1), (-1, 0), (0, 1)]
answer = 0
for hubo in hubos:
    tmp = 0
    new_arr = deepcopy(arr)
    while True:
        die = set()
        rest_enemy = 0
        for a in hubo:
            flag = 0
            q = deque([(n, a, 0)])
            while q:
                ci, cj, dist = q.popleft()
                for di, dj in dlt:
                    ni, nj = ci+di, cj+dj
                    if 0 <= ni < n and 0 <= nj < m:
                        if new_arr[ni][nj] == 1:
                            die.add((ni, nj))
                            flag = 1
                            break
                        else:
                            if dist + 1 < d:
                                q.append((ni, nj, dist + 1))
                if flag:
                    break
        for i in range(n-1, -1, -1):
            for j in range(m):
                if new_arr[i][j] == 1:
                    if (i, j) in die:
                        tmp += 1
                    elif i < n-1:
                        rest_enemy += 1
                        new_arr[i+1][j] = 1
                    new_arr[i][j] = 0
        if rest_enemy == 0:
            break
    if tmp > answer:
        answer = tmp
print(answer)