from itertools import combinations
for _ in range(int(input())):
    n = input()
    l = len(n)
    answer = 0
    m = 1
    for char in n:
        if char != '0' and char != '1':
            break
    else:
        print("Hello, BOJ 2023!")
        continue
    while True:
        ssum = sum(map(lambda x:int(x)**m, n))
        if ssum > int(n):
            break
        flag = False
        for i in range(l):
            for plus in combinations(range(1, l), i):
                right = 0
                idx = 0
                tmp = 0
                while idx < l:
                    if idx in plus:
                        right += tmp
                        tmp = int(n[idx])
                    else:
                        tmp = tmp * 10 + int(n[idx])
                    idx += 1
                right += tmp
                if ssum == right:
                    flag = True
                    break
            if flag:
                break
        if flag:
            answer += 1
        m += 1
    print(answer)