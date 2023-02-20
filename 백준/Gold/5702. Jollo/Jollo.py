while True:
    g1, g2, g3, b1, b2 = map(int, input().split())
    if g1 == g2 == g3 == b1 == b2 == 0:
        break
    cards = (g1, g2, g3, b1, b2)
    gs = sorted([g1, g2, g3])
    bs = sorted([b1, b2])
    checked = [0] * 3
    for b in range(1, -1, -1):
        for g in range(3):
            if checked[g] == 0 and gs[g] > bs[b]:
                checked[g] = 2
                break
        else:
            if checked[0]:
                checked[1] = 1
            else:
                checked[0] = 1
    answer = -1
    if sum(checked) >= 4:
        answer = -1
    else:
        if sum(checked) <= 2:
            answer = 1
        else:
            for i in range(3):
                if checked[i] == 0:
                    answer = gs[i] + 1
        while answer in cards:
            answer += 1
        if answer >= 53:
            answer = -1
    print(answer)