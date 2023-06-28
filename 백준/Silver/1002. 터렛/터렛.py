t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if r2 > r1:
        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        # 작은 원이 큰 원 안에 있는 경우
        if (x1 - x2) ** 2 + (y1 - y2) ** 2 < r1 ** 2:
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 == (r1 - r2) ** 2:
                print(1)
            elif (x1 - x2) ** 2 + (y1 - y2) ** 2 > (r1 - r2) ** 2:
                print(2)
            else:
                print(0)
        # 아닌 경우
        else:
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 == (r1 + r2) ** 2:
                print(1)
            elif (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 + r2) ** 2:
                print(2)
            else:
                print(0)