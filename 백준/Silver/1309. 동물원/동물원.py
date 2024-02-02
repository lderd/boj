n = int(input())
l = 1
r = 1
c = 1
for _ in range(n-1):
    l, r, c = (c+r) % 9901, (c+l) % 9901, (c+r+l)% 9901
print((l+c+r)% 9901)