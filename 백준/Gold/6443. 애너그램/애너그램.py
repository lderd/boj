def solve(idx, ans):
    if idx >= l:
        print(ans)
        return
    for i in range(l):
        if not checked[i] and check[idx] < word[i]:
            ch = word[i]
            if idx == l - 1:
                print(ans + ch)
                continue
            check[idx] = ch
            checked[i] = True
            solve(idx + 1, ans + ch)
            checked[i] = False
    check[idx] = '-'


n = int(input())
for _ in range(n):
    word = sorted(list(input()))
    l = len(word)
    check = ['-'] * l
    checked = [False] * l
    solve(0, '')