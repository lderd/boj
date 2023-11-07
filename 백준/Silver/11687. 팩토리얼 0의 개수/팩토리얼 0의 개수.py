m = int(input())
s = 0
e = 500000000
answer = -1
while s <= e:
    mid = (s + e) // 2
    two = 0
    tmp = mid
    while tmp:
        two += tmp // 2
        tmp //= 2
    five = 0
    tmp = mid
    while tmp:
        five += tmp // 5
        tmp //= 5
    zero = min(two, five)
    if zero == m:
        answer = mid
        e = mid - 1
    elif zero > m:
        e = mid - 1
    else:
        s = mid + 1
print(answer)