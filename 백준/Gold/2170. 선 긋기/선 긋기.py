import sys
input = sys.stdin.readline
n = int(input())
line = []
for _ in range(n):
    a, b = map(int, input().split())
    line.append((a, b))
line.sort()
answer = 0
s = -1000000001
e = -1000000001
for a, b in line:
    if a > e:
        answer += e - s
        s = a
        e = b
    else:
        if b > e:
            e = b
answer += e - s
print(answer)