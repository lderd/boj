a = input()
b = input()
c = input()
alen = len(a)
blen = len(b)
clen = len(c)
if clen > blen:
    b, c, blen, clen = c, b, clen, blen
if alen < blen:
    b, a, blen, alen = a, b, alen, blen
if clen > blen:
    b, c, blen, clen = c, b, clen, blen
cnt = [[0] * alen for _ in range(blen)]
for char in c:
    tmp = [[0] * alen for _ in range(blen)]
    for i in range(blen):
        for j in range(alen):
            if char == b[i] == a[j]:
                if i == 0 or j == 0:
                    tmp[i][j] = 1
                else:
                    tmp[i][j] = max(tmp[i][j-1], cnt[i-1][j-1] + 1)
            else:
                if i == 0:
                    if j == 0:
                        tmp[i][j] = cnt[i][j]
                    else:
                        tmp[i][j] = max(cnt[i][j], tmp[i][j-1])
                elif j == 0:
                    tmp[i][j] = cnt[i][j]
                else:
                    tmp[i][j] = max(tmp[i][j-1], cnt[i][j], tmp[i-1][j])
    cnt = tmp
print(max(max(cnt[i]) for i in range(blen)))