from bisect import bisect_left, bisect_right
n, h = map(int, input().split())
bottom = []
bottom_l = 0
top = []
for i in range(n):
    if i % 2:
        top.append(h - int(input()))
    else:
        bottom.append(int(input()))
        bottom_l += 1
top.sort()
bottom.sort()
cnt = 200001
answer = 0
for i in range(h):
    tmp_cnt = bottom_l - bisect_right(bottom, i) + bisect_left(top, i + 1)
    if tmp_cnt < cnt:
        cnt = tmp_cnt
        answer = 1
    elif tmp_cnt == cnt:
        answer += 1
print(cnt, answer)