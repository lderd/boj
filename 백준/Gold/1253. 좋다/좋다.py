from bisect import bisect_left
from collections import defaultdict
n = int(input())
a = sorted(map(int, input().split()))
answer = 0
check = defaultdict(bool)
for i in range(n):
    number = a[i]
    if check[number]:
        answer += 1
        continue
    for j in range(n):
        if i == j: continue
        left = bisect_left(a, number - a[j])
        if left < n and a[j] + a[left] == number:
            if a[left] == a[j] == a[i]:
                if left < n - 2 and a[left] == a[left + 1] == a[left + 2]:
                    check[number] = True
                    answer += 1
                    break
            elif a[left] == a[i]:
                if left < n - 1 and a[left] == a[left + 1]:
                    check[number] = True
                    answer += 1
                    break
            elif a[left] == a[j]:
                if left < n - 1 and a[left] == a[left + 1]:
                    check[number] = True
                    answer += 1
                    break
            else:
                check[number] = True
                answer += 1
                break
print(answer)