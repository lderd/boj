import sys
from bisect import bisect_right
input = sys.stdin.readline
n = int(input())
answer = 1
arr = [int(input()) for _ in range(n)]
sorted_arr = sorted(arr)
for i in range(n):
    idx = bisect_right(sorted_arr, arr[i])
    if i - idx + 2 > answer:
        answer = i - idx + 2
print(answer)