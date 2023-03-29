def extend_euclid(b):
    a = 1000000007
    bs, bt = 1, 0
    cs, ct = 0, 1
    while True:
        if a > b:
            q = a // b
            a %= b
            ns, nt = bs - cs * q, bt - ct * q
        elif b > a:
            q = b // a
            b %= a
            ns, nt = bs - cs * q, bt - ct * q
        bs, bt = cs, ct
        cs, ct = ns, nt
        if a == 0 or b == 0:
            return (bt + 1000000007) % 1000000007


n, m, k = map(int, input().split())
arr = []
tree = [[1, 0, 1] for _ in range(n + 1)]
for i in range(1, n + 1):
    num = int(input())
    if num == 0:
        arr.append([num, 0])
        while i <= n:
            tree[i][1] += 1
            i += i & -i
    else:
        inverse = extend_euclid(num)
        arr.append([num, inverse])
        while i <= n:
            tree[i][0] *= num
            tree[i][0] %= 1000000007

            tree[i][2] *= inverse
            tree[i][2] %= 1000000007

            i += i & -i

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        i = b
        if arr[b - 1][0] == c:
            continue
        else:
            if arr[b - 1][0] == 0:
                inverse = extend_euclid(c)
                while i <= n:
                    tree[i][1] -= 1

                    tree[i][0] *= c
                    tree[i][0] %= 1000000007

                    tree[i][2] *= inverse
                    tree[i][2] %= 1000000007

                    i += i & -i
                arr[b - 1] = [c, inverse]
            else:
                if c == 0:
                    while i <= n:
                        tree[i][0] *= arr[b - 1][1]
                        tree[i][0] %= 1000000007

                        tree[i][2] *= arr[b - 1][0]
                        tree[i][2] %= 1000000007

                        tree[i][1] += 1
                        i += i & -i

                    arr[b - 1] = [0, 0]
                else:
                    inverse = extend_euclid(c)
                    while i <= n:
                        tree[i][0] *= arr[b - 1][1]
                        tree[i][0] *= c
                        tree[i][0] %= 1000000007

                        tree[i][2] *= arr[b - 1][0]
                        tree[i][2] *= inverse
                        tree[i][2] %= 1000000007

                        i += i & -i
                    arr[b - 1] = [c, inverse]
    if a == 2:
        answer = 1
        zero_cnt = 0
        i = c
        while i >= 1:
            answer *= tree[i][0]
            answer %= 1000000007
            zero_cnt += tree[i][1]
            i -= i & -i
        i = b - 1
        while i >= 1:
            answer *= tree[i][2]
            answer %= 1000000007
            zero_cnt -= tree[i][1]
            i -= i & -i
        if zero_cnt:
            print(0)
        else:
            print(answer % 1000000007)