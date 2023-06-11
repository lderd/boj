from collections import defaultdict
from heapq import heappush, heappop
t = int(input())
for _ in range(t):
    k = int(input())
    plus = []
    minus = []
    check = defaultdict(int)
    for _ in range(k):
        operator, num = input().split()
        if operator == 'I':
            num = int(num)
            check[num] += 1
            heappush(minus, num)
            heappush(plus, -num)
        else:
            if num == '-1':
                while minus:
                    min_val = heappop(minus)
                    if check[min_val]:
                        check[min_val] -= 1
                        break
            else:
                while plus:
                    max_val = heappop(plus) * (-1)
                    if check[max_val]:
                        check[max_val] -= 1
                        break
    max_val = '0'
    min_val = '0'
    while minus:
        min_tmp = heappop(minus)
        if check[min_tmp]:
            min_val = min_tmp
            break
    while plus:
        max_tmp = heappop(plus) * (-1)
        if check[max_tmp]:
            max_val = max_tmp
            break
    if max_val != '0' and min_val != '0':
        print(f'{max_val} {min_val}')
    else:
        print('EMPTY')