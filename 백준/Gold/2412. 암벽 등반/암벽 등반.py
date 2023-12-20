from collections import deque
import sys
n, t = map(int, input().split())
wall = [set() for _ in range(t+1)]
q = deque([(0, 0, 0)])
for _ in range(n):
    x, y = map(int, input().split())
    wall[y].add(x)
checked = {(0, 0)}
while q:
    cx, cy, cnt = q.popleft()
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            nx, ny = cx+dx, cy+dy
            if 0 <= ny <= t and nx in wall[ny] and (nx, ny) not in checked:
                if ny == t:
                    print(cnt + 1)
                    sys.exit()
                checked.add((nx, ny))
                q.append((nx, ny, cnt+1))
print(-1)