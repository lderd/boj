from functools import reduce
tmp, cnt = reduce(lambda acc, cur: [cur, acc[1]] if acc[0] == cur else [cur, acc[1] + 1], input(), ['2', -1])
print((cnt + 1) // 2)