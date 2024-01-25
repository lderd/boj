a = input()
b = input()
la = len(a)
cnt = [0] * la
for char in b:
    tmp = [0] * la
    for i in range(la):
        if char == a[i]:
            if i == 0:
                tmp[i] = 1
            else:
                tmp[i] = max(tmp[i-1], cnt[i-1]+1)
        else:
            tmp[i] = max(cnt[i], tmp[i-1])
    cnt = tmp
print(cnt[-1])