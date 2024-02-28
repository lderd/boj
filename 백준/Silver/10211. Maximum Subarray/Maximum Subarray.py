import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = -10000000
    tmp = 0
    for num in arr:
        tmp += num
        if tmp > answer:
            answer = tmp
        if tmp < 0:
            tmp = 0
    print(answer)