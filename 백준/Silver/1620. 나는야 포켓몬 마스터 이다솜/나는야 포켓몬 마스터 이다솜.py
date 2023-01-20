import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dogam = [input().strip() for _ in range(n)]
for _ in range(m):
    problem = input().strip()
    if problem.isalpha():
        print(dogam.index(problem)+1)
    else:
        print(dogam[int(problem)-1])