from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
l = 0
tmp = []
for num in arr:
    idx = bisect_left(tmp, num)
    if idx >= l:
        tmp.append(num)
        l += 1
    else:
        tmp[idx] = num
print(l)