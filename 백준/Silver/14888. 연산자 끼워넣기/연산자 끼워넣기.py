def solve(idx, val, plus, minus, mul, div):
    global max_answer, min_answer
    if idx >= n:
        if val > max_answer:
            max_answer = val
        if val < min_answer:
            min_answer = val
        return
    if plus < oper[0]:
        solve(idx+1, val+a[idx], plus+1, minus, mul, div)
    if minus < oper[1]:
        solve(idx+1, val-a[idx], plus, minus+1, mul, div)
    if mul < oper[2]:
        solve(idx+1, val*a[idx], plus, minus, mul+1, div)
    if div < oper[3]:
        if val < 0:
            solve(idx+1, -(-val // a[idx]), plus, minus, mul, div+1)
        else:
            solve(idx+1, val // a[idx], plus, minus, mul, div+1)


n = int(input())
a = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_answer = -1000000000
min_answer = 1000000000
solve(1, a[0], 0, 0, 0, 0)
print(max_answer)
print(min_answer)