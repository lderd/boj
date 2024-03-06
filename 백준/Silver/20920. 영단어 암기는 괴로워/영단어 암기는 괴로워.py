from collections import defaultdict
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cnt = defaultdict(int)
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        cnt[word] += 1
answer = list(cnt.keys())
answer.sort(key=lambda x:[-cnt[x], -len(x), x])
for ans in answer:
    print(ans)