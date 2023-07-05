from copy import deepcopy
t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    new_arr = deepcopy(arr)
    d //= 45
    if d == 1 or d == -7:
        for i in range(n):
            new_arr[i][n//2] = arr[i][i]
            new_arr[n//2][n-1-i] = arr[i][n-1-i]
            new_arr[i][n-1-i] = arr[i][n//2]
            new_arr[i][i] = arr[n//2][i]
    elif d == 2 or d == -6:
        for i in range(n):
            new_arr[i][n-1-i] = arr[i][i]
            new_arr[n-1-i][n-1-i] = arr[i][n-1-i]
            new_arr[n//2][n-1-i] = arr[i][n//2]
            new_arr[i][n//2] = arr[n//2][i]
    elif d == 3 or d == -5:
        for i in range(n):
            new_arr[n//2][n-1-i] = arr[i][i]
            new_arr[n-1-i][n//2] = arr[i][n-1-i]
            new_arr[n-1-i][n-1-i] = arr[i][n//2]
            new_arr[i][n-1-i] = arr[n//2][i]
    elif d == 4 or d == -4:
        for i in range(n):
            new_arr[n-1-i][n-1-i] = arr[i][i]
            new_arr[n-1-i][i] = arr[i][n-1-i]
            new_arr[n-1-i][n//2] = arr[i][n//2]
            new_arr[n//2][n-1-i] = arr[n//2][i]
    elif d == 5 or d == -3:
        for i in range(n):
            new_arr[n-1-i][n//2] = arr[i][i]
            new_arr[n//2][i] = arr[i][n-1-i]
            new_arr[n-1-i][i] = arr[i][n//2]
            new_arr[n-1-i][n-1-i] = arr[n//2][i]
    elif d == 6 or d == -2:
        for i in range(n):
            new_arr[n-1-i][i] = arr[i][i]
            new_arr[i][i] = arr[i][n-1-i]
            new_arr[n//2][i] = arr[i][n//2]
            new_arr[n-1-i][n//2] = arr[n//2][i]
    elif d == 7 or d == -1:
        for i in range(n):
            # 주대각 i i
            # 부대각 i n-1-i
            # 세로 i n//2
            # 가로 n//2 i
            new_arr[n//2][i] = arr[i][i]
            new_arr[i][n//2] = arr[i][n-1-i]
            new_arr[i][i] = arr[i][n//2]
            new_arr[n-1-i][i] = arr[n//2][i]
    for i in range(n):
        print(*new_arr[i])