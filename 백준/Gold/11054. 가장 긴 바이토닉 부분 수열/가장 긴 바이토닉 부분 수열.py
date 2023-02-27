n = int(input())
arr = list(map(int, input().split()))
check = [[0, 0] for _ in range(n)]
check[0] = [1, 0]
answer = 1
for i in range(1, n):
    big = 0
    small = 0
    for j in range(i):
        if arr[j] < arr[i] and check[j][0] > big:
            big = check[j][0]
        elif arr[j] > arr[i] and max(check[j]) > small:
            small = max(check[j])
        if max(big + 1, small + 1) > answer:
            answer = max(big+1, small+1)
    check[i] = [big+1, small+1]
print(answer)