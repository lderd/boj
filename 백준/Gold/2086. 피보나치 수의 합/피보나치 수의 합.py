from collections import defaultdict
def S(n):
    if n == 0:
        return 0
    if memoS[n] == 0:
        memoS[n] = (F(n//2+1) * S((n+1)//2) % 1000000000 + F(n//2) * S((n-1)//2) % 1000000000 + S(n//2)) % 1000000000
    return memoS[n]


def F(n):
    if n == 0:
        return 0
    if memoF[n] == 0:
        memoF[n] = (F(n//2+1)*F((n+1)//2) % 1000000000 + F(n//2) * F((n-1)//2) % 1000000000) % 1000000000
    return memoF[n]


a, b = map(int, input().split())
memoS = defaultdict(int)
memoF = defaultdict(int)
memoS[1] = memoF[1] = memoF[2] = 1
memoS[2] = 2
print((S(b) - S(a-1) + 1000000000) % 1000000000)