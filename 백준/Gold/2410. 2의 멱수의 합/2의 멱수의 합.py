n = int(input())
idx = 0
arr = [1]
for _ in range(n//2):
    tmp = arr[-1]
    arr.append((tmp + arr[idx]) % 1000000000)
    arr.append((tmp + arr[idx]) % 1000000000)
    idx += 1
print(arr[n-1])