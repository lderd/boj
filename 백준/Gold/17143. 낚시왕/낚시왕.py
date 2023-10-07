r, c, m = map(int, input().split())
# z크기, d방향, s속력
arr = [[[0, 0, 0] for _ in range(c)] for _ in range(r)]
sharks = set()
for _ in range(m):
    i, j, s, d, z = map(int, input().split())
    sharks.add((i-1, j-1))
    arr[i-1][j-1] = [z, d, s]
answer = 0
for kj in range(c):
    new_arr = [[[0, 0, 0] for _ in range(c)] for _ in range(r)]
    for ki in range(r):
        if arr[ki][kj][0] > 0:
            answer += arr[ki][kj][0]
            sharks.remove((ki, kj))
            break
    new_sharks = set()
    for i, j in sharks:
#     z크기, d방향, s속력
        z, d, s = arr[i][j]
        origin_s = s
#      1위     2아래    3오른쪽   4왼쪽
        if d == 1:
            if s > i:
                s -= i
                cnt = s // (r - 1)
                rest = s % (r - 1)
                if cnt % 2:
                    i = r - 1 - rest
                    if rest == 0:
                        d = 2
                else:
                    d = 2
                    i = rest
                    if rest == 0:
                        d = 1
            else:
                i -= s
#      1위     2아래    3오른쪽   4왼쪽
        elif d == 2:
            if s > r - 1 - i:
                s -= r - 1 - i
                cnt = s // (r - 1)
                rest = s % (r - 1)
                if cnt % 2:
                    i = rest
                    if rest == 0:
                        d = 1
                else:
                    d = 1
                    i = r - 1 - rest
                    if rest == 0:
                        d = 2
            else:
                i += s
#      1위     2아래    3오른쪽   4왼쪽
        elif d == 3:
            if s > c - 1 - j:
                s -= c - 1 - j
                cnt = s // (c - 1)
                rest = s % (c - 1)
                if cnt % 2:
                    j = rest
                    if rest == 0:
                        d = 4
                else:
                    d = 4
                    j = c - 1 - rest
                    if rest == 0:
                        d = 3
            else:
                j += s
#      1위     2아래    3오른쪽   4왼쪽
        else:
            if s > j:
                s -= j
                cnt = s // (c - 1)
                rest = s % (c - 1)
                if cnt % 2:
                    j = c - 1 - rest
                    if rest == 0:
                        d = 3
                else:
                    d = 3
                    j = rest
                    if rest == 0:
                        d = 4
            else:
                j -= s
        if new_arr[i][j][0] < z:
            new_arr[i][j] = [z, d, origin_s]
        new_sharks.add((i, j))
    arr = new_arr
    sharks = new_sharks
print(answer)