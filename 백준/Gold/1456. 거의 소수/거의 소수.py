from math import sqrt
a, b = map(int, input().split())
end = int(sqrt(b)) + 1
arr = set(range(2, end + 1))
answer = set()
for i in range(2, end // 2 + 1):
    tmp = i + i
    while True:
        if tmp > end:
            break
        if tmp in arr:
            arr.remove(tmp)
        tmp += i
for i in arr:
    tmp = i * i
    while True:
        if a <= tmp <= b:
            answer.add(tmp)
        elif tmp > b:
            break
        tmp *= i
print(len(answer))