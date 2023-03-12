def f(num):
    arr = [0] * 51
    for i in range(51):
        arr[i] = num // (2 ** i)
        if i >= 1:
            arr[i-1] -= arr[i]
    answer = 0
    for i in range(51):
        if arr[i] == 0:
            break
        answer += 2 ** i * arr[i]
    return answer


a, b = map(int, input().split())
print(f(b) - f(a - 1))