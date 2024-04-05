import sys
input = sys.stdin.readline
n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for i in range(n):
    flag = False
    h = arr[i][0]
    cnt = 1
    for j in range(1, n):
        if flag:
            if arr[i][j] == h:
                cnt += 1
                if cnt >= l:
                    cnt -= l
                    flag = False
            else:
                break
        else:
            if h - 1 <= arr[i][j] <= h + 1:
                if arr[i][j] < h:
                    flag = True
                    h = arr[i][j]
                    cnt = 1
                    if cnt >= l:
                        cnt -= l
                        flag = False
                elif arr[i][j] > h:
                    if cnt >= l:
                        h = arr[i][j]
                        cnt = 1
                    else:
                        break
                else:
                    cnt += 1
            else:
                break
    else:
        if not flag:
            answer += 1
for j in range(n):
    flag = False
    h = arr[0][j]
    cnt = 1
    for i in range(1, n):
        if flag:
            if arr[i][j] == h:
                cnt += 1
                if cnt >= l:
                    cnt -= l
                    flag = False
            else:
                break
        else:
            if h - 1 <= arr[i][j] <= h + 1:
                if arr[i][j] < h:
                    flag = True
                    h = arr[i][j]
                    cnt = 1
                    if cnt >= l:
                        cnt -= l
                        flag = False
                elif arr[i][j] > h:
                    if cnt >= l:
                        h = arr[i][j]
                        cnt = 1
                    else:
                        break
                else:
                    cnt += 1
            else:
                break
    else:
        if not flag:
            answer += 1
print(answer)