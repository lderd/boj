N = int(input())
K = int(input())
sensors = sorted(list(set(map(int, input().split()))))
gaps = []
for i in range(len(sensors)-1):
    gaps.append(sensors[i+1] - sensors[i])
gaps.sort()
answer = 0
cnt = len(sensors)
i = 0
while cnt > K:
    cnt -= 1
    answer += gaps[i]
    i += 1
print(answer)