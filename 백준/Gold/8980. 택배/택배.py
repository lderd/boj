import sys
input = sys.stdin.readline
n, c = map(int, input().split())
m = int(input())
up = [0] * (n + 1)
down = [0] * (n + 1)
for i in range(m):
    s, e, box = map(int, input().split())
    up[s] += box
    down[e] += box
answer = 0
now = 0
for i in range(n + 1):
    if now >= down[i]:
        now -= down[i]
        answer += down[i]
    else:
        if now > 0:
            answer += now
            now = 0
    if now + up[i] <= c:
        now += up[i]
    else:
        if now < c:
            now = c
print(answer)