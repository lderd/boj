import sys
input = sys.stdin.readline
m, n = map(int, input().split())
needs = [int(input()) for _ in range(n)]
needs.sort(reverse=True)
minus = [0] * n
idx = 0
while m > 0:
    if idx < n - 1:
        gap = needs[idx] - needs[idx+1]
        idx += 1
        if m >= gap * idx:
            minus[idx-1] += gap
            m -= gap * idx
        else:
            gap = m // idx
            minus[idx-1] += gap
            m %= idx
            if m:
                minus[m-1] += 1
                m -= m
    else:
        idx += 1
        gap = m // idx
        minus[idx-1] += gap
        m -= gap * idx
        if m:
            minus[m-1] += 1
            m -= m
answer = 0
tmp = 0
for i in range(n-1, -1, -1):
    tmp += minus[i]
    answer += (needs[i] - tmp) ** 2
    answer %= 2**64
print(answer)