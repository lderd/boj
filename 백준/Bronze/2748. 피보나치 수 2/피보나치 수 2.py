n = int(input())
num = 1
memo = [0, 1]
while num < n:
    num += 1
    memo.append(memo[-1]+memo[-2])
print(memo[n])