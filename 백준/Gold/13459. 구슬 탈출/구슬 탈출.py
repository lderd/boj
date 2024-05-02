from collections import deque
import sys
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
red = (-1, -1)
blue = (-1, -1)
for i in range(1, n-1):
    for j in range(1, m-1):
        if arr[i][j] == 'R':
            red = (i, j)
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            blue = (i, j)
            arr[i][j] = '.'
checked = {(*red, *blue)}
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque([(*red, *blue, 0)])
while q:
    redi, redj, bluei, bluej, cnt = q.popleft()
    for idx in range(4):
        first = (redi, redj)
        second = (bluei, bluej)
        flag = False
        # 위로 간다, i가 더 작은 구슬 먼저
        if idx == 0 and redi > bluei:
            first = (bluei, bluej)
            second = (redi, redj)
            flag = True
        # 아래로 간다. i가 더 큰 구슬 먼저
        elif idx == 1 and redi < bluei:
            first = (bluei, bluej)
            second = (redi, redj)
            flag = True
        # 왼쪽으로 간다. j가 더 작은 구슬 먼저
        elif idx == 2 and redj > bluej:
            first = (bluei, bluej)
            second = (redi, redj)
            flag = True
        # 오른쪽으로 간다. j가 더 큰 구슬 먼저
        elif idx == 3 and redj < bluej:
            first = (bluei, bluej)
            second = (redi, redj)
            flag = True
        di, dj = d[idx]
        for k in range(1, 10):
            if arr[first[0] + di * k][first[1] + dj * k] == 'O':
                first = (first[0] + di * k, first[1] + dj * k)
                break
            if arr[first[0] + di * k][first[1] + dj * k] == '#':
                first = (first[0] + di * (k - 1), first[1] + dj * (k - 1))
                break
        for k in range(1, 10):
            if arr[second[0] + di * k][second[1] + dj * k] == 'O':
                second = (second[0] + di * k, second[1] + dj * k)
                break
            if arr[second[0] + di * k][second[1] + dj * k] == '#' or (second[0] + di * k, second[1] + dj * k) == first:
                second = (second[0] + di * (k - 1), second[1] + dj * (k - 1))
                break
        if flag:
            red = second
            blue = first
        else:
            red = first
            blue = second
        if arr[blue[0]][blue[1]] == 'O':
            continue
        if arr[red[0]][red[1]] == 'O':
            print(1)
            sys.exit()
        if cnt < 9 and (*red, *blue) not in checked:
            checked.add((*red, *blue))
            q.append((*red, *blue, cnt+1))
print(0)