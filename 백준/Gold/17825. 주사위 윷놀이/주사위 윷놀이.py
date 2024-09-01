def go(idx, score, a, b, c, d):
    global answer
    if idx >= 10:
        if score > answer:
            answer = score
        return
    dice = dices[idx]
    position = {a, b, c, d}
    if a != end_point:
        new_a = move(a, dice, True)
        if new_a == end_point or new_a not in position:
            aa, bb, cc, dd = sorted([new_a, b, c, d])
            new_score = score + scores[new_a[0]][new_a[1]][new_a[2]]
            go(idx + 1, new_score, aa, bb, cc, dd)
    if b != end_point:
        new_b = move(b, dice, True)
        if new_b == end_point or new_b not in position:
            new_score = score + scores[new_b[0]][new_b[1]][new_b[2]]
            aa, bb, cc, dd = sorted([a, new_b, c, d])
            go(idx + 1, new_score, aa, bb, cc, dd)
    if c != end_point:
        new_c = move(c, dice, True)
        if new_c == end_point or new_c not in position:
            new_score = score + scores[new_c[0]][new_c[1]][new_c[2]]
            aa, bb, cc, dd = sorted([a, b, new_c, d])
            go(idx + 1, new_score, aa, bb, cc, dd)
    if d != end_point:
        new_d = move(d, dice, True)
        if new_d == end_point or new_d not in position:
            aa, bb, cc, dd = sorted([a, b, c, new_d])
            new_score = score + scores[new_d[0]][new_d[1]][new_d[2]]
            go(idx + 1, new_score, aa, bb, cc, dd)


def move(p, cnt, start):
    x, y, z = p
    if cnt == 0: return (x, y, z)
    # 일반 길 위에 있다
    if x == 0:
        if z == 5:
            if y == 3:
                return end_point
            # 지름길로 들어간다
            if start:
                y = scores[x][y][z] // 10 - 1
                return move((1, y, 1), cnt - 1, False)
            else:
                return move((0, y + 1, 1), cnt - 1, False)
        # 한 칸 앞으로 간다
        else:
            return move((0, y, z + 1), cnt - 1, False)
    # 지름길 위에 있다
    else:
        if y == 0:
            # 넘어간다
            if z == 3:
                return move((1, 3, 1), cnt - 1, False)
            # 다음 칸으로
            else:
                return move((x, y, z + 1), cnt - 1, False)
        elif y == 1:
            # 넘어간다
            if z == 2:
                return move((1, 3, 1), cnt - 1, False)
            # 다음 칸으로
            else:
                return move((x, y, z + 1), cnt - 1, False)
        elif y == 2:
            # 넘어간다
            if z == 3:
                return move((1, 3, 1), cnt - 1, False)
            # 다음 칸으로
            else:
                return move((x, y, z + 1), cnt - 1, False)
        elif y == 3:
            # 넘어간다
            if z == 3:
                return move((0, 3, 5), cnt - 1, False)
            # 다음 칸으로
            else:
                return move((x, y, z + 1), cnt - 1, False)


dices = list(map(int, input().split()))
checked = set()
answer = 0
scores = [[[0, 2, 4, 6, 8, 10],
           [0, 12, 14, 16, 18, 20],
           [0, 22, 24, 26, 28, 30],
           [0, 32, 34, 36, 38, 40, 0]],
          [[0, 13, 16, 19],
           [0, 22, 24],
           [0, 28, 27, 26],
           [0, 25, 30, 35]]]
end_point = (0, 3, 6)
go(0, 0, (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
print(answer)