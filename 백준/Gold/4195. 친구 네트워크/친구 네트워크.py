from collections import defaultdict
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
        return a
    else:
        p[a] = b
        return b


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


t = int(input())
for _ in range(t):
    f = int(input())
    p = list(range(2*f+1))
    network = [set() for _ in range(2*f+1)]
    name_index = defaultdict(int)
    index = 1
    for _ in range(f):
        a, b = input().split()
        if name_index[a] == 0:
            name_index[a] = index
            index += 1
        if name_index[b] == 0:
            name_index[b] = index
            index += 1
        a_index = find(name_index[a])
        b_index = find(name_index[b])
        if a_index != b_index:
            idx = union(a_index, b_index)
            network[idx].add(a)
            network[idx].add(b)
            if idx != a:
                network[idx] |= network[a_index]
            if idx != b:
                network[idx] |= network[b_index]
        print(len(network[find(a_index)]))