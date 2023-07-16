n, s = map(int, input().split())
arr = list(map(int, input().split()))
i = j = 0
ssum = 0
answer = 100001
while j < n:
    ssum += arr[j]
    while ssum >= s and i <= j:
        if j - i + 1 < answer:
            answer = j - i + 1
        ssum -= arr[i]
        i += 1
    j += 1
if answer == 100001:
    print(0)
else:
    print(answer)