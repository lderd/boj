'''
0 1  2  3 4 5
1 3  5  7 9
1 9 25 49
(idx + 1) * 2 - 3 ** 2 + 1 => 첫번째 숫자
(idx + 1) * 2 - 1 ** 2 => 마지막 숫자
'''
def find(r, c):
    idx = max(abs(r), abs(c))
    start = ((idx + 1) * 2 - 3) ** 2 + 1
    value = 1
    # 오른쪽
    if c == idx and r < idx:
        value = start + idx - 1 - r
    # 위쪽
    if r == -idx and c < idx:
        value = start + (idx * 2) + idx - 1 - c
    # 왼쪽
    if c == -idx and r > -idx:
        value = start + (idx * 2) * 2 + r + idx - 1
    # 아래쪽
    if r == idx and c > -idx:
        value = start + (idx * 2) * 3 + c + idx - 1
    return str(value)


r1, c1, r2, c2 = map(int, input().split())
answer = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
max_len = 0
j = 0
for c in range(c1, c2 + 1):
    i = 0
    for r in range(r1, r2 + 1):
        answer[i][j] = find(r, c)
        if max_len < len(answer[i][j]):
            max_len = len(answer[i][j])
        i += 1
    j += 1
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(answer[i][j].rjust(max_len, " "), end=" ")
    print()