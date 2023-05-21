n = int(input())
coins = [list(map(lambda x: '1' if x == 'T' else '0', input())) for _ in range(n)]
coins = list(map(lambda x: int(''.join(x), 2), coins))

answer = sum(map(lambda x: bin(x).count('1'), coins))
row = (1 << n) - 1
for reverse in range(1, 1<<n):
    tmp = 0
    n_coin = coins[:]
    for i in range(n):
        n_coin[i] = (n_coin[i] | reverse) - (n_coin[i] & reverse)
    for i in range(n):
        tmp += min(bin(n_coin[i]).count('1'), bin((n_coin[i] | row) - (n_coin[i] & row)).count('1'))
    if answer > tmp:
        answer = tmp

print(answer)