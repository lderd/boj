import sys
sys.setrecursionlimit(2000000)
input = sys.stdin.readline
def find_circle(now, before):
    global circle
    for new in graph[now]:
        if new != before and new in tmp_checked:
            circle = set(tmp_circle[tmp_circle.index(new):])
            return
        if new not in full_checked:
            full_checked.add(new)
            tmp_checked.add(new)
            tmp_circle.append(new)
            find_circle(new, now)
            tmp_checked.remove(new)
            tmp_circle.pop()
        if circle:
            return

def root_check(a, r):
    for new in graph[a]:
        if new not in full_checked:
            full_checked.add(new)
            p[new] = r
            root_check(new, r)


n, q = map(int, input().split())
graph = [[] for _ in range(n)]
parent = list(range(n))
for _ in range(n):
    a, b = map(lambda x:int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)
circle = set()
full_checked = {0}
tmp_checked = {0}
tmp_circle = [0]
find_circle(0, -1)
full_checked.clear()
full_checked |= circle
p = list(range(n))
for r in circle:
    root_check(r, r)
for _ in range(q):
    a, b = map(lambda x:int(x)-1, input().split())
    if p[a] == p[b]:
        print(1)
    else:
        print(2)