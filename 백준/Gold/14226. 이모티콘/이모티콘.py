from collections import deque, defaultdict
n = int(input())
checked = defaultdict(set)
q = deque([(1, 0, 0)])
while q:
    num, cnt, saved = q.popleft()
    if num - 1 > 1 and saved not in checked[num-1]:
        if num - 1 == n:
            print(cnt + 1)
            break
        checked[num-1].add(saved)
        q.append((num-1, cnt+1, saved))
    if num not in checked[num]:
        checked[num].add(num)
        q.append((num, cnt+1, num))
    if saved not in checked[num + saved]:
        if num + saved == n:
            print(cnt + 1)
            break
        checked[num+saved].add(saved)
        q.append((num+saved, cnt+1, saved))