import sys
input = sys.stdin.readline
n = int(input())
big = 0
answer = ""
for _ in range(n):
    num, ans, nation = input().split()
    if nation == "Russia" and big < int(num):
        big = int(num)
        answer = ans
print(answer)