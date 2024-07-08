'''
힌트를 좀 받음.
노드를 기준으로 푸는게 아니라 간선을 기준으로 문제를 해결한다.
ㄷ의 경우 가운데 간선의 좌우로 뻗어나갈 수 있는 간선의 수를 곱하면 간선이 가운데에 들어가는 ㄷ트리를 모두 찾을 수 있다.
즉, 2개의 이웃한 노드에서 각각 뻗어나가는 간선의 수를 찾아 두 수를 곱한다.
ㅈ의 경우 노드에서 뻗어나가는 간선의 수가 3개 이상이면 된다.
ㄷ은 왼쪽 노드 수 * 오른쪽 노드 수
ㅈ은 뻗어나가는 간선 중에 3개를 선택하는 방법
일종의 조합
'''
import sys
input = sys.stdin.readline

n = int(input())
near = [[0] for _ in range(n)]
for _ in range(n-1):
    a, b = map(lambda x:int(x) - 1, input().split())
    near[a].append(b)
    near[a][0] += 1
    near[b].append(a)
    near[b][0] += 1
d = 0
g = 0
for i in range(n):
    l = near[i][0]
    if l >= 3:
        g += l * (l - 1) * (l - 2)
    for idx in range(1, near[i][0] + 1):
        daum = near[i][idx]
        d += (l - 1) * (near[daum][0] - 1)
if d > g:
    print('D')
elif d < g:
    print('G')
elif d == g:
    print('DUDUDUNGA')