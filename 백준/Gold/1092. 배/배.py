n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
crane.sort(reverse=True)
box.sort(reverse=True)
cnt = [0] * n
if crane[0] < box[0]:
    print(-1)
else:
    for i in range(m):
        tmp = 99999999999
        index = 0
        for j in range(n):
            if crane[j] < box[i]:
                break
            if cnt[j] < tmp:
                index = j
                tmp = cnt[j]
        cnt[index] += 1
    print(max(cnt))