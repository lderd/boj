def search(l, r, v):
    if l > r:
        return l
    mid = (l + r) // 2
    if tmp_v[mid] >= v:
        return search(l, mid - 1, v)
    else:
        return search(mid + 1, r, v)


n = int(input())
arr = []
A = set()
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    A.add(a)
arr.sort()

pre_index = [-1] * n
tmp_v = [arr[0][1]]
tmp_i = [0]
length = 1

pre_index[0] = 0

for i in range(n):
    a, b = arr[i]
    index = search(0, length-1, b)
    if index == 0:
        tmp_v[0] = b
        tmp_i[0] = i
        pre_index[i] = i
    elif index >= length:
        tmp_v.append(b)
        tmp_i.append(i)
        pre_index[i] = tmp_i[index-1]
        length += 1
    else:
        tmp_v[index] = b
        tmp_i[index] = i
        pre_index[i] = tmp_i[index-1]
print(n - length)
remain = set()
now = tmp_i[length-1]
while True:
    remain.add(arr[now][0])
    if now == pre_index[now]:
        break
    now = pre_index[now]
answer = sorted(list(A - remain))
for i in answer:
    print(i)