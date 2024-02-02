import sys
input = sys.stdin.readline
memo = [[0] * 31 for _ in range(31)]
memo[1][0] = 1
for cnt in range(1, 60):
    for h_cnt in range(cnt):
        if cnt - h_cnt < h_cnt: break
        w_cnt = cnt - h_cnt
        if w_cnt >= h_cnt + 1 and w_cnt <= 30 and h_cnt < 30:
            memo[w_cnt][h_cnt + 1] += memo[w_cnt][h_cnt]
        if w_cnt < 30 and h_cnt <= 30:
            memo[w_cnt + 1][h_cnt] += memo[w_cnt][h_cnt]
while True:
    n = int(input())
    if n == 0: break
    print(memo[n][n])