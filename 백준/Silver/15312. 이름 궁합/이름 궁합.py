a = input()
b = input()
dp = []
cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
l = len(a) * 2
for a_char, b_char in zip(a, b):
    dp.append(cnt[ord(a_char)-65])
    dp.append(cnt[ord(b_char)-65])
while l > 2:
    tmp = []
    for i in range(l-1):
        tmp.append((dp[i]+dp[i+1])%10)
    dp = tmp
    l -= 1
print(f'{dp[0]}{dp[1]}')
