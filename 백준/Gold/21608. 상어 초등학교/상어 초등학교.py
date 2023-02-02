N = int(input())
arr = [[0] * N for _ in range(N)]
students = []
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for _ in range(N**2):
    student, friend1, friend2, friend3, friend4 = map(int, input().split())
    friends = {friend1, friend2, friend3, friend4}
    students.append([student, friends])
    si = sj = 0
    blank = 0
    friend_cnt = 0
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if arr[i][j] == 0:
                blank_tmp = 0
                friend_cnt_tmp = 0
                for di, dj in d:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] == 0:
                            blank_tmp += 1
                        elif arr[ni][nj] in friends:
                            friend_cnt_tmp += 1
                if friend_cnt < friend_cnt_tmp:
                    si = i
                    sj = j
                    friend_cnt = friend_cnt_tmp
                    blank = blank_tmp
                elif friend_cnt == friend_cnt_tmp:
                    if blank <= blank_tmp:
                        si = i
                        sj = j
                        blank = blank_tmp
    arr[si][sj] = student
students.sort()
answer = 0
for i in range(N):
    for j in range(N):
        tmp = 0
        for di, dj in d:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in students[arr[i][j]-1][1]:
                    tmp += 1
        if tmp > 0:
            answer += 10 ** (tmp-1)
print(answer)