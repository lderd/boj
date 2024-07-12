a, b = map(int, input().split())
tmp = sum(range(1, a+1))
answer = tmp
for i in range(a+1, b+1):
    tmp += i
    tmp %= 14579
    answer *= tmp
    answer %= 14579
print(answer)