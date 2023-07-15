n = int(input())
a = int(input())
arr = map(int, input().split())
time = 0
q = []
for number in arr:
    for i in range(len(q)):
        if q[i][2] == number:
            q[i][0] += 1
            break
    else:
        if len(q) < n:
            q.append([1, time, number])
            time += 1
        else:
            tmp_cnt = 1001
            tmp_t = 1001
            tmp = 0
            for i in range(n):
                if q[i][0] < tmp_cnt or (q[i][0] == tmp_cnt and q[i][1] < tmp_t):
                    tmp_cnt = q[i][0]
                    tmp_t = q[i][1]
                    tmp = i
            q[tmp] = [1, time, number]
            time += 1
q.sort(key=lambda x: x[2])
for _, _, ans in q:
    print(ans, end=' ')