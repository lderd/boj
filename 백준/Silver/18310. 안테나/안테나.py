n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
dist = 100000000000
for ans in range(n//2-1, n//2+1):
    if 0 <= ans < n:
        tmp = 0
        p = arr[ans]
        for i in arr:
            tmp += abs(p - i)
        if tmp < dist:
            answer = ans
            dist = tmp
print(arr[answer])