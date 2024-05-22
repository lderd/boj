n = int(input())
arr = [-1] * (n + 1)
if n >= 2:
    arr[2] = 1
if n >= 5:
    arr[5] = 1
for i in range(2, n-1):
    if arr[i] > 0:
        if i + 2 <= n and (arr[i + 2] == -1 or arr[i] + 1 < arr[i + 2]):
            arr[i + 2] = arr[i] + 1
        if i + 5 <= n and (arr[i + 5] == -1 or arr[i] + 1 < arr[i + 5]):
            arr[i + 5] = arr[i] + 1
print(arr[n])