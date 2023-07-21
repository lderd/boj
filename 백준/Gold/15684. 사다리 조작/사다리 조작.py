'''
0 1 2 3 4 5 6 7 8 9
0 1   2   3   4   5
1   1
2 2   1   3   4   5
3           1
4 2   1   4   3   5
5       1
6 2   4   1   3   5
7
8 2   4   1   3   5
9   1           1
0 4   2   1   5   3
1
2 4   2   1   5   3



1   2   3
  1
2   1   3
      1
2   3   1
  1
3   2   1
  1
2   3   1




3 3 30
1 1
2 2
3 1
'''
import sys
from itertools import combinations
from copy import deepcopy

def down(the_ladder):
    for i in range(1, n + 1):
        the_ladder[0][2*i-1] = i
    for i in range(1, h + 1):
        for j in range(n):
            if 2 * j + 2 < n * 2 and the_ladder[2 * i - 1][2 * j + 2] == 1:
                the_ladder[2 * i][2 * j + 1] = the_ladder[2 * i - 2][2 * j + 3]
            elif 2 * j > 0 and the_ladder[2 * i - 1][2 * j] == 1:
                the_ladder[2 * i][2 * j + 1] = the_ladder[2 * i - 2][2 * j - 1]
            else:
                the_ladder[2 * i][2 * j + 1] = the_ladder[2 * i - 2][2 * j + 1]
    ret = []
    for i in range(1, n + 1):
        ret.append(the_ladder[2 * h][2 * i - 1])
    return ret


n, m, h = map(int, input().split())
ladder = [[0] * (2 * n) for _ in range(2 * h + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    ladder[2*a-1][2*b] = 1
tmp = down(ladder)
cnt = 0
dismatch = set()
for i in range(n):
    if tmp[i] != i + 1:
        dismatch.add(i + 1)
for i in range(n):
    if tmp[i] == i + 1: continue
    index = tmp.index(i + 1)
    tmp[i], tmp[index] = tmp[index], tmp[i]
    cnt += 1
if cnt == 0:
    print(0)
    sys.exit()
elif cnt > 3:
    print(-1)
    sys.exit()
hubo = []
for i in range(h):
    for j in range(1, n):
        if ladder[2 * i + 1][2*j] == 0 and (ladder[2 * i][2 * j - 1] in dismatch or ladder[2 * i][2 * j + 1] in dismatch):
            if 2 * j - 2 > 0 and ladder[2 * i][2 * j - 2] == 1:
                continue
            elif 2 * j + 2 < 2 * n and ladder[2 * i][2 * j + 2] == 1:
                continue
            else:
                hubo.append((i, j))

for ans in range(1, 4):
    for tuples in combinations(hubo, ans):
        flag = 0
        for i in range(ans):
            for j in range(i + 1, ans):
                if tuples[i][0] == tuples[j][0] and -1 <= tuples[i][1] - tuples[j][1] <= 1:
                    flag = 1
                    break
            if flag:
                break
        if flag:
            continue
        the_ladder = deepcopy(ladder)
        for i, j in tuples:
            the_ladder[2 * i + 1][2*j] = 1
            if list(range(1, n + 1)) == down(the_ladder):
                print(ans)
                sys.exit()
print(-1)