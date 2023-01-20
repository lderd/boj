'''
A[:1] = 1
A[i] = A[i//p - x] + A[i//q - y]
'''
from collections import defaultdict
def solve(i):
    if i <= 0:
        return 1
    if A[i]:
        return A[i]
    A[i] = solve(i//p-x) + solve(i//q-y)
    return A[i]

n, p, q, x, y = map(int, input().split())
A = defaultdict(int)
A[0] = 1
print(solve(n))