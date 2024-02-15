while True:
    try:
        n, k = map(int, input().split())
        X = list(map(int, input().split()))
        cnt = [0] * (n+1)
        zero = [0] * (n+1)
        answer = ''
        for i in range(1, n+1):
            if X[i-1] < 0:
                while i <= n:
                    cnt[i] += 1
                    cnt[i] %= 2
                    i += i & -i
            elif X[i-1] == 0:
                while i <= n:
                    zero[i] += 1
                    i += i & -i
        for _ in range(k):
            order, *numbers = input().split()
            if order == 'C':
                i, v = map(int, numbers)
                if v < 0:
                    if X[i-1] >= 0:
                        ii = i
                        while ii <= n:
                            cnt[ii] += 1
                            cnt[ii] %= 2
                            ii += ii & -ii
                        if X[i-1] == 0:
                            ii = i
                            while ii <= n:
                                zero[ii] -= 1
                                ii += ii & -ii
                        X[i-1] = v
                elif v == 0:
                    if X[i-1] != 0:
                        ii = i
                        while ii <= n:
                            zero[ii] += 1
                            ii += ii & -ii
                        if X[i-1] < 0:
                            ii = i
                            while ii <= n:
                                cnt[ii] += 1
                                cnt[ii] %= 2
                                ii += ii & -ii
                        X[i-1] = 0
                else:
                    if X[i-1] < 0:
                        ii = i
                        while ii <= n:
                            cnt[ii] += 1
                            cnt[ii] %= 2
                            ii += ii & -ii
                        X[i-1] = v
                    elif X[i-1] == 0:
                        ii = i
                        while ii <= n:
                            zero[ii] -= 1
                            ii += ii & -ii
                        X[i-1] = v
            else:
                i, j = map(int, numbers)
                zero_cnt = 0
                minus_cnt = 0
                e = j
                while e > 0:
                    zero_cnt += zero[e]
                    minus_cnt += cnt[e]
                    e -= e & -e
                s = i - 1
                while s > 0:
                    zero_cnt -= zero[s]
                    minus_cnt -= cnt[s]
                    s -= s & -s
                if zero_cnt:
                    answer += '0'
                else:
                    if minus_cnt % 2:
                        answer += '-'
                    else:
                        answer += '+'
        print(answer)
    except:
        break