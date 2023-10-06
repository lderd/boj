import sys
n, k = input().split()
k = int(k)
l = len(n)
if l < k:
    print('5' * k)
elif l == k:
    answer = '5' * l
    if answer > n:
        print(answer)
    else:
        print('1' + answer)
else:
    n = str(int(n) + 1)
    cnt = 0
    for num in n:
        if num == '5':
            cnt += 1
    if cnt >= k:
        print(n)
        sys.exit()
    nk = k
    l = len(n)
    idx = 0
    while idx < l - k and k > 0:
        if n[idx] == '5':
            k -= 1
        idx += 1
    flag = True
    for i in range(idx, l):
        if n[i] < '5':
            flag = False
            break
        elif n[i] > '5':
            break
    if flag:
        n = str(int(n) - 1)
        tmp = str(int(n[:idx]) + 1) + '0' * k
        l = len(tmp)
        nidx = 0
        while nidx < l - nk and nk > 0:
            if tmp[nidx] == '5':
                nk -= 1
            nidx += 1
        print(tmp[:nidx] + '0' * (l-nk-nidx) + '5' * nk)
    else:
        print(n[:idx] + '5' * k)