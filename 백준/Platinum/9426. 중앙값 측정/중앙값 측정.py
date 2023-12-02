import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, k = map(int, input().split())
small = []
small_size = 1
big = []
big_size = 0
tmp = int(input())
tmp_idx = 0
arr = [tmp]
if k == 1:
    answer = tmp
else:
    answer = 0
for i in range(1, n):
    t = int(input())
    arr.append(t)
    # 넣고, 뺴고, 중심 맞추기
    # 넣고
    if t >= tmp:
        big_size += 1
        heappush(big, (t, i))
    else:
        small_size += 1
        heappush(small, (-t, i))

    # 빼고
    pop_idx = i - k
    if pop_idx >= 0:
        # 현재 중간값, small, big 최상단이 제외할 값이다
        small_num, small_idx = -1, -1
        if small:
            small_num, small_idx = small[0]
        big_num, big_idx = -1, -1
        if big:
            big_num, big_idx = big[0]

        if big_idx == pop_idx:
            heappop(big)
            big_size -= 1
        elif small_idx == pop_idx:
            heappop(small)
            small_size -= 1
        elif tmp_idx == pop_idx:
            while small:
                small_num, small_idx = heappop(small)
                if small_idx <= pop_idx: continue
                tmp = -small_num
                tmp_idx = small_idx
                small_size -= 1
                break
            if tmp_idx == pop_idx:
                while big:
                    big_num, big_idx = heappop(big)
                    if big_idx <= pop_idx: continue
                    tmp = big_num
                    tmp_idx = big_idx
                    big_size -= 1
                    break

        # 제외할 값이 왼쪽에 있다.
        elif arr[pop_idx] < tmp:
            small_size -= 1
        # 제외할 값이 오른쪽에 있다.
        elif arr[pop_idx] > tmp:
            big_size -= 1
    # 중심맞추기
    while small_size > big_size + 1:
        small_num, small_idx = heappop(small)
        if small_idx <= pop_idx: continue
        small_size -= 1
        heappush(big, (tmp, tmp_idx))
        big_size += 1
        tmp = -small_num
        tmp_idx = small_idx
    while small_size < big_size:
        big_num, big_idx = heappop(big)
        if big_idx <= pop_idx: continue
        big_size -= 1
        heappush(small, (-tmp, tmp_idx))
        small_size += 1
        tmp = big_num
        tmp_idx = big_idx
    if i >= k-1:
        answer += tmp
print(answer)