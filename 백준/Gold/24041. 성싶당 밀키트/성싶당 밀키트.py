import sys
input = sys.stdin.readline
n, g, k = map(int, input().split())
core_materials = []
not_core_materials = []
not_len = 0
for _ in range(n):
    s, l, o = map(int, input().split())
    if o:
        not_core_materials.append((s, l))
        not_len += 1
    else:
        core_materials.append((s, l))
start = 0
end = 10000000000
while start <= end:
    mid = (start + end) // 2
    virus = 0
    no = []
    for s, l in core_materials:
        virus += s * max(1, mid - l)
    for s, l in not_core_materials:
        no.append(s * max(1, mid - l))
    no.sort()
    if not_len > k:
        virus += sum(no[:not_len - k])
    if virus > g:
        end = mid - 1
    else:
        start = mid + 1
print(end)