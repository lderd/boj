from bisect import bisect_left
n = int(input())
arr = list(map(int, input().split()))
length = 1
s = [arr[0]]
for i in range(n):
    index = bisect_left(s, arr[i])
    if index >= length:
        s.append(arr[i])
        length += 1
    else:
        s[index] = arr[i]
print(length)