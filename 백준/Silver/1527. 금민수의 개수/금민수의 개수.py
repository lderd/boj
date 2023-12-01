a, b = input().split()
len_a = len(a)
len_b = len(b)
answer = 0
for l in range(1, len_b+1):
    memo = [[0, 0] for _ in range(l)]
    if l == len_b:
        for num in ['4', '7']:
            if b[0] > num:
                memo[0][0] += 1
            elif b[0] == num:
                memo[0][1] += 1
        for i in range(l-1):
            for num in ['4', '7']:
                if b[i+1] > num:
                    memo[i+1][0] += memo[i][1]
                elif b[i+1] == num:
                    memo[i+1][1] += memo[i][1]
                memo[i+1][0] += memo[i][0]
        answer += sum(memo[-1])
    else:
        memo[0] = [2, 0]
        for i in range(l-1):
            memo[i+1][0] += memo[i][0] * 2
        answer += memo[-1][0]
for l in range(1, len_a+1):
    memo = [[0, 0] for _ in range(l)]
    if l == len_a:
        for num in ['4', '7']:
            if a[0] > num:
                memo[0][0] += 1
            elif a[0] == num:
                memo[0][1] += 1
        for i in range(l-1):
            for num in ['4', '7']:
                if a[i+1] > num:
                    memo[i+1][0] += memo[i][1]
                elif a[i+1] == num:
                    memo[i+1][1] += memo[i][1]
                memo[i+1][0] += memo[i][0]
        answer -= memo[-1][0]
    else:
        memo[0] = [2, 0]
        for i in range(l-1):
            memo[i+1][0] += memo[i][0] * 2
        answer -= memo[-1][0]
print(answer)