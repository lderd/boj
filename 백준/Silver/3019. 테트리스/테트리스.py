c, p = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
if p == 1:
    answer += c
    for i in range(3, c):
        if arr[i-3] == arr[i-2] == arr[i-1] == arr[i]:
            answer += 1
elif p == 2:
    for i in range(1, c):
        if arr[i - 1] == arr[i]:
            answer += 1
elif p == 3:
    for i in range(1, c):
        if i > 1 and arr[i-2] == arr[i-1] == arr[i] - 1:
            answer += 1
        if arr[i-1] - 1 == arr[i]:
            answer += 1
elif p == 4:
    for i in range(1, c):
        if i > 1 and arr[i-2] - 1 == arr[i-1] == arr[i]:
            answer += 1
        if arr[i-1] + 1 == arr[i]:
            answer += 1
elif p == 5:
    for i in range(1, c):
        if i > 1:
            if arr[i-2] == arr[i-1] == arr[i]:
                answer += 1
            elif arr[i-2] == arr[i] == arr[i-1] + 1:
                answer += 1
        if arr[i-1] == arr[i] + 1:
            answer += 1
        elif arr[i-1] + 1 == arr[i]:
            answer += 1
elif p == 6:
    for i in range(1, c):
        if i > 1:
            if arr[i-2] == arr[i-1] == arr[i]:
                answer += 1
            elif arr[i-2] + 1 == arr[i-1] == arr[i]:
                answer += 1
        if arr[i-1] == arr[i]:
            answer += 1
        elif arr[i-1] == arr[i] + 2:
            answer += 1
else:
    for i in range(1, c):
        if i > 1:
            if arr[i-2] == arr[i-1] == arr[i]:
                answer += 1
            elif arr[i-2] == arr[i-1] == arr[i] + 1:
                answer += 1
        if arr[i-1] == arr[i]:
            answer += 1
        elif arr[i-1] + 2 == arr[i]:
            answer += 1
print(answer)