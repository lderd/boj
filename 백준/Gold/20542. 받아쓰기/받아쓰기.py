my_len, ans_len = map(int, input().split())
my = input()
ans = input()
tmp = list(range(ans_len + 1))
memo = [0] * ans_len
for i in range(ans_len):
    if i == 0:
        if ans[i] == my[0] or ((ans[i] == 'j' or ans[i] == 'l') and my[0] == 'i') or (ans[i] == 'w' and my[0] == 'v'):
            memo[i] = tmp[i]
        else:
            memo[i] = min(tmp[i] + 1, tmp[i+1] + 1)
    else:
        if ans[i] == my[0] or ((ans[i] == 'j' or ans[i] == 'l') and my[0] == 'i') or (ans[i] == 'w' and my[0] == 'v'):
            memo[i] = min(tmp[i], tmp[i + 1], memo[i-1] + 1)
        else:
            memo[i] = min(tmp[i] + 1, tmp[i+1] + 1, memo[i-1] + 1)
for i in range(1, my_len):
    tmp = [0] * ans_len
    for j in range(ans_len):
        if j == 0:
            if ans[j] == my[i] or ((ans[j] == 'j' or ans[j] == 'l') and my[i] == 'i') or (ans[j] == 'w' and my[i] == 'v'):
                tmp[j] = i
            else:
                tmp[j] = min(i + 1, memo[j] + 1)
        else:
            if ans[j] == my[i] or ((ans[j] == 'j' or ans[j] == 'l') and my[i] == 'i') or (ans[j] == 'w' and my[i] == 'v'):
                tmp[j] = memo[j-1]
            else:
                tmp[j] = min(memo[j-1] + 1, memo[j] + 1, tmp[j-1] + 1)
    memo = tmp
print(memo[ans_len-1])