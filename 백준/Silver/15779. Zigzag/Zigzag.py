n = int(input())
arr = list(map(int, input().split()))
s = 0
e = 1
answer = 1
last = ''
while e < n:
    tmp = str()
    if arr[e] > arr[e-1]:
        tmp = '+'
    elif arr[e] < arr[e-1]:
        tmp = '-'
    else:
        tmp = '='
    if last == '=' or tmp == '=' or last == tmp:
        s = e - 1
    if answer < e - s + 1:
        answer = e - s + 1
    last = tmp
    e += 1
print(answer)