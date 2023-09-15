from heapq import heappop, heappush
n, k = map(int, input().split())
seq = list(map(int, input().split()))
ele = [[1] for _ in range(k + 1)]
answer = 0
plugin_check = set()
plugin = []
for i in range(k):
    e = seq[i]
    ele[e].append(i)
for e in seq:
    if len(plugin_check) < n:
        plugin_check.add(e)
        # 나오는 순서가 나중인 것을 먼저 뺼거다 + 남은 횟수가 0이면 제일 먼저 뺀다
        # -> 나중인걸 먼저 뺀다 -> 순서가 큰 걸 먼저 -> -index인데 0이면 제일 먼저 빼야하니까
        # 0일때는 -101
        ele[e][0] += 1
        e_cnt = ele[e][0]
        if len(ele[e]) > e_cnt:
            heappush(plugin, (-ele[e][e_cnt], e))
        else:
            heappush(plugin, (-101, e))
    else:
        if e in plugin_check:
            ele[e][0] += 1
            e_cnt = ele[e][0]
            if len(ele[e]) > e_cnt:
                heappush(plugin, (-ele[e][e_cnt], e))
            else:
                heappush(plugin, (-101, e))
        else:
            next_use, el = heappop(plugin)
            while el not in plugin_check and plugin:
                next_use, el = heappop(plugin)
            if el in plugin_check:
                answer += 1
                plugin_check.remove(el)
                plugin_check.add(e)
                ele[e][0] += 1
                e_cnt = ele[e][0]
                if len(ele[e]) > e_cnt:
                    heappush(plugin, (-ele[e][e_cnt], e))
                else:
                    heappush(plugin, (-101, e))
print(answer)
