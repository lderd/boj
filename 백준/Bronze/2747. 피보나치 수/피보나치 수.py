n = int(input())
memo = [0, 1]
num = 1
while num < n:
    memo.append(memo[-1]+memo[-2])
    num += 1
print(memo[n])