import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ts = sorted([int(input()) for _ in range(n)])
s = 0
e = ts[0] * m + 1
answer = 0
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for t in ts:
        cnt += mid // t
        if cnt >= m:
            answer = mid
            e = mid - 1
            break
    else:
        s = mid + 1
print(answer)