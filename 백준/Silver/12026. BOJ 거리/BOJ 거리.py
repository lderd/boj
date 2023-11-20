def solve(i):
    tmp = dist[i]
    for idx in range(i+1, n):
        if block[i] == 'B':
            if block[idx] == 'O' and (dist[idx] == -1 or tmp + (idx - i) * (idx - i) < dist[idx]):
                dist[idx] = tmp + (idx - i) * (idx - i)
                solve(idx)
        elif block[i] == 'O':
            if block[idx] == 'J' and (dist[idx] == -1 or tmp + (idx - i) * (idx - i) < dist[idx]):
                dist[idx] = tmp + (idx - i) * (idx - i)
                solve(idx)
        else:
            if block[idx] == 'B' and (dist[idx] == -1 or tmp + (idx - i) * (idx - i) < dist[idx]):
                dist[idx] = tmp + (idx - i) * (idx - i)
                solve(idx)


n = int(input())
block = input()
dist = [-1] * n
dist[0] = 0
solve(0)
print(dist[n-1])