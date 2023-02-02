tc = 0
while True:
    tc += 1
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    answer = L * (V // P)
    if V % P <= L:
        answer += V % P
    else:
        answer += L
    print(f'Case {tc}: {answer}')