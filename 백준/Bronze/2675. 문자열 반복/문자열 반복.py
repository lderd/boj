t = int(input())
for _ in range(t):
    cnt, char = input().split()
    cnt = int(cnt)
    for i in char:
        print(i * cnt, end='')
    print()