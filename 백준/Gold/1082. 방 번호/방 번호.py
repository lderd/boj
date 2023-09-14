n = int(input())
ps = list(map(int, input().split()))
m = int(input())
a = [[] for _ in range(m + 1)]
answer = -1
for money in range(1, m+1):
    a[money] = a[money-1]
    for i in range(n):
        p = ps[i]
        if money - p >= 0:
            if len(a[money]) == 0:
                a[money] = a[money - p] + [str(i)]
            if int(''.join(sorted(a[money - p] + [str(i)], reverse=True))) > int(''.join(a[money])):
                a[money] = sorted(a[money - p] + [str(i)], reverse=True)
print(''.join(a[m]))