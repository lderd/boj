n, b, w = map(int, input().split())
road = input()
answer = 0
b_cnt = 0
w_cnt = 0
s = 0
e = 0
while e < n:
    if road[e] == 'W':
        w_cnt += 1
    else:
        b_cnt += 1
        while b_cnt > b and s <= e:
            if road[s] == 'W':
                w_cnt -= 1
                s += 1
            else:
                b_cnt -= 1
                s += 1
    if w_cnt >= w and b_cnt + w_cnt > answer:
        answer = b_cnt + w_cnt
    e += 1
print(answer)