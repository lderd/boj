n, k = map(int, input().split())
tmp_list = list(map(int, input().split()))
arr = []
tmp = 0
for num in tmp_list:
    if num % 2:
        arr.append(tmp)
        tmp = 0
    else:
        tmp += 1
if tmp:
    arr.append(tmp)
s = 0
e = 1
cnt = 0
answer = arr[0]
tmp = arr[0]
while e < len(arr):
    tmp += arr[e]
    cnt += 1
    if cnt > k:
        tmp -= arr[s]
        cnt -= 1
        s += 1
    if tmp > answer:
        answer = tmp
    e += 1
print(answer)