def down(time, position, fire):
    global answer
    new_fire = [0] * n
    cnt = 0
    for i in range(n):
        tmp = 0
        if fire[i] <= 0:
            continue
        if i == position:
            new_fire[i] = fire[i]
        else:
            if i > 0:
                if fire[i-1] > 0:
                    tmp += 1
            if i < n - 1:
                if fire[i+1] > 0:
                    tmp += 1

            if tmp == 0:
                new_fire[i] = fire[i] - 3
            elif tmp == 1:
                new_fire[i] = fire[i] - 2
            elif tmp == 2:
                new_fire[i] = fire[i] - 1

        if new_fire[i] > 0:
            cnt += 1
    if cnt < k:
        return
    if time >= t:
        answer += 1
        return
    move(time + 1, position, new_fire)


def move(time, position, fire):
    down(time, position, fire)
    if position > 0:
        down(time, position - 1, fire)
    if position < n - 1:
        down(time, position + 1, fire)


# 모닥불 수n, 시작 모닥불 번호m, 놀이시간 t, 유지해야하는 k
n, w, t, k = map(int, input().split())
F = list(map(int, input().split()))
answer = 0
new_fire = [0] * n
cnt = 0
for i in range(n):
    tmp = 0
    if i > 0:
        if F[i - 1] > 0:
            tmp += 1
    if i < n - 1:
        if F[i + 1] > 0:
            tmp += 1
    if tmp == 0:
        new_fire[i] = F[i] - 3
    elif tmp == 1:
        new_fire[i] = F[i] - 2
    elif tmp == 2:
        new_fire[i] = F[i] - 1

    if new_fire[i] > 0:
        cnt += 1
if t == 1:
    if cnt >= k:
        answer += 1
else:
    if cnt >= k:
        move(2, w, new_fire)
print(answer)