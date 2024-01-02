import sys
input = sys.stdin.readline
s, c = map(int, input().split())
start = 1
end = 0
ls = []
for _ in range(s):
    l = int(input())
    ls.append(l)
    if end < l:
        end = l
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in ls:
        cnt += l // mid
        if cnt >= c:
            start = mid + 1
            break
    else:
        end = mid - 1
answer = 0
if end == 0:
    for l in ls:
        answer += l
    print(answer)
else:
    cnt = 0
    for l in ls:
        cnt += l // end
        answer += l % end
    answer += (cnt - c) * end
    print(answer)