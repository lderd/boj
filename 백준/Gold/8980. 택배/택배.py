import sys
input = sys.stdin.readline
n, c = map(int, input().split())
m = int(input())
boxes = [[0] * 2 for _ in range(n)]
for i in range(m):
    s, e, box = map(int, input().split())
    boxes[s - 1][0] += box
    boxes[e - 1][1] += box
answer = 0
now = 0
for i in range(n):
    up, down = boxes[i]
    if down:
        if now >= down:
            now -= down
            answer += down
        else:
            if now > 0:
                answer += now
                now = 0
    if up and now < c:
        if now + up <= c:
            now += up
        else:
            now = c
print(answer)