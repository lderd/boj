n, red, green, blue = map(int, input().split())
tree = [[[[0] * min(56, blue + 1) for _ in range(min(56, green + 1))] for _ in range(min(56, red + 1))] for _ in range(n+1)]
tree[0][red][green][blue] = 1
answer = 0
cnt = 1
cnt2 = 1
cnt3 = 1
for step in range(1, n + 1):
    cnt *= step
    if step % 2 == 0:
        cnt2 *= step // 2 * step // 2
    if step % 3 == 0:
        cnt3 *= step // 3 * step // 3 * step // 3
    for r in range(red + 1):
        for g in range(green + 1):
            for b in range(blue + 1):
                if tree[step - 1][r][g][b] > 0:
                    if r >= step:
                        tree[step][r - step][g][b] += tree[step - 1][r][g][b]
                    if g >= step:
                        tree[step][r][g - step][b] += tree[step - 1][r][g][b]
                    if b >= step:
                        tree[step][r][g][b - step] += tree[step - 1][r][g][b]
                    if step % 2 == 0:
                        divide2 = step // 2
                        if r >= divide2:
                            if g >= divide2:
                                tree[step][r-divide2][g-divide2][b] += tree[step - 1][r][g][b] * cnt // cnt2
                            if b >= divide2:
                                tree[step][r-divide2][g][b-divide2] += tree[step - 1][r][g][b] * cnt // cnt2
                        if g >= divide2 and b >= divide2:
                            tree[step][r][g-divide2][b-divide2] += tree[step - 1][r][g][b] * cnt // cnt2
                    if step % 3 == 0:
                        divide3 = step // 3
                        if r >= divide3 and g >= divide3 and b >= divide3:
                            tree[step][r-divide3][g-divide3][b-divide3] += tree[step-1][r][g][b] * cnt // cnt3
for r in range(red + 1):
    for g in range(green + 1):
        for b in range(blue + 1):
            answer += tree[n][r][g][b]
print(answer)