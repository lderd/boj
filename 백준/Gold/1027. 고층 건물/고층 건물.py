n = int(input())
buildings = list(map(int, input().split()))
answer = 0
for i in range(n):
    cnt = 0
    j = i - 1
    minus = -1000000000
    while j >= 0:
        d = (buildings[j] - buildings[i]) / (i - j)
        if minus < d:
            cnt += 1
            minus = d
        j -= 1
    j = i + 1
    plus = -1000000000
    while j < n:
        d = (buildings[j] - buildings[i]) / (j - i)
        if plus < d:
            cnt += 1
            plus = d
        j += 1
    if answer < cnt:
        answer = cnt
print(answer)