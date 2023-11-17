n = int(input())
s = list(map(int, input().split()))
s.sort()
answer = 1
for num in s:
    if answer < num:
        break
    answer += num
print(answer)