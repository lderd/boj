t = int(input())
for _ in range(t):
    n = int(input())
    one = set(input().split())
    m = int(input())
    two = input().split()
    for num in two:
        print(1 if num in one else 0)