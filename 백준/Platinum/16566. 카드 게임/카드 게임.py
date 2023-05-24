from bisect import bisect_right
from math import sqrt

n, m, k = map(int, input().split())
bundle_size = int(sqrt(n))

cards = sorted(list(map(int, input().split())))
exist = [True] * m

bundle_index = [0] * m
bundles = [[0, 0, 0] for _ in range(bundle_size + 2)]
for i in range(m):
    index = cards[i] // bundle_size
    bundle_index[i] = index
    if bundles[index][0] == 0:
        bundles[index][1] = i
    bundles[index][0] += 1
    bundles[index][2] = i

popList = list(map(int, input().split()))
for popCard in popList:
    index = bisect_right(cards, popCard)
    bundle_i = cards[index] // bundle_size
    while bundles[bundle_i][0] <= 0:
        bundle_i += 1
    min_index = bundles[bundle_i][1]
    max_index = bundles[bundle_i][2]
    if index < min_index:
        index = min_index
    for i in range(index, max_index + 1):
        if exist[i]:
            print(cards[i])
            exist[i] = False
            bundles[bundle_i][0] -= 1
            break
    else:
        bundle_i += 1
        while bundles[bundle_i][0] <= 0:
            bundle_i += 1
        min_index = bundles[bundle_i][1]
        max_index = bundles[bundle_i][2]
        if index < min_index:
            index = min_index
        for i in range(index, max_index + 1):
            if exist[i]:
                print(cards[i])
                exist[i] = False
                bundles[bundle_i][0] -= 1
                break