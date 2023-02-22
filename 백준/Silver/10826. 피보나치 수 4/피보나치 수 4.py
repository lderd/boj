n = int(input())
memo = [0, 1, 1, 2]
cnt = 3
while cnt < n:
    cnt += 1
    memo.append(memo[-1] + memo[-2])
print(memo[n])