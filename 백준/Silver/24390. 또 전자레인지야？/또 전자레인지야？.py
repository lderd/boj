h, m = map(int, input().split(':'))
m += 60 * h
answer = 0
answer += m // 600
m %= 600
answer += m // 60
m %= 60
flag = 1
answer += m // 30
if m // 30:
    flag = 0
m %= 30
answer += m // 10
print(answer + flag)