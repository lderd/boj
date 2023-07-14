from collections import deque
n = int(input())
tmp = [set() for _ in range(n+1)]
checked = [True] * (n + 1)
# (부모노드, 깊이)
tree = list(map(lambda x: (x, 0),range(n+1)))
for _ in range(n-1):
    p, c = map(int, input().split())
    tmp[p].add(c)
    tmp[c].add(p)
q = deque([(1, 0)])
checked[1] = False
while q:
    now, depth = q.popleft()
    for i in tmp[now]:
        if checked[i]:
            tree[i] = (now, depth + 1)
            q.append((i, depth + 1))
            checked[i] = False
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    ap, ad = tree[a]
    bp, bd = tree[b]
    if a == b:
        ap = a
    else:
        while ap != bp:
            if ad < bd:
                if a == bp:
                    ap = a
                    break
                bp, bd = tree[bp]
            elif ad > bd:
                if b == ap:
                    ap = b
                    break
                ap, ad = tree[ap]
            else:
                ap, ad = tree[ap]
                bp, bd = tree[bp]
    print(ap)