import sys
input = sys.stdin.readline
while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        answer = -1
        l1 = -1
        l2 = -1
        ls = set()
        for _ in range(n):
            l = int(input())
            if l != x // 2 and l in ls: continue
            if x - l in ls:
                tmp_l1 = min(l, x - l)
                tmp_l2 = max(l, x - l)
                if tmp_l2 - tmp_l1 > answer:
                    answer = tmp_l2 - tmp_l1
                    l1 = tmp_l1
                    l2 = tmp_l2
            ls.add(l)
        if answer == -1:
            print('danger')
        else:
            print(f'yes {l1} {l2}')
    except:
        break