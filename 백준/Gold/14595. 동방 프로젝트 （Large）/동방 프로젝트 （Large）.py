import sys
input = sys.stdin.readline

n = int(input())
room = [0] * n
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    room[x-1] += 1
    room[y-1] -= 1

answer = 0
tmp = 0
for i in range(n):
    tmp += room[i]
    if tmp == 0:
        answer += 1
print(answer)