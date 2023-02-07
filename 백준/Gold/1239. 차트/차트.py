from itertools import permutations
n = int(input())
arr = map(int, input().split())
hubo = set(permutations(arr, n))
answer = 0
for combi in hubo:
    combi = list(combi) + list(combi)[:-1]
    s = 0
    e = 0

    ssum = combi[0]

    tmp = 0
    while s < n and s <= e and e < 2 * n - 1:
        if ssum == 50:
            tmp += 1
            s += 1
            e += 1
            if e < 2 * n - 1:
                ssum = ssum - combi[s-1] + combi[e]
        elif ssum < 50:
            e += 1
            if e < 2 * n - 1:
                ssum += combi[e]
        elif ssum > 50:
            s += 1
            if s <= n and s <= e:
                ssum -= combi[s-1]
    if tmp > answer:
        answer = tmp
print(answer//2)