# 부품수
n = int(input())
# 부품관계
m = int(input())
cnt = [0] * (n + 1)
relation = dict()
for _ in range(m):
    x, y, k = map(int, input().split())
    cnt[x] += 1
    if not relation.get(y):
        relation[y] = {}
    relation[y][x] = k
answer = dict()
q = []
for i in range(1, n+1):
    if cnt[i] == 0:
        answer[i] = {i:1}
        q.append(i)
while q:
    part = q.pop()
    if not relation.get(part): continue
    for i, k in relation[part].items():
        cnt[i] -= 1
        if cnt[i] == 0:
            q.append(i)
        if not answer.get(i):
            answer[i] = {}
        for j, kk in answer[part].items():
            if not answer[i].get(j):
                answer[i][j] = 0
            answer[i][j] += k * kk
for i in sorted(answer[n]):
    print(i, answer[n][i])