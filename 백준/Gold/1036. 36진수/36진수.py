def dec_to_cus(num):
    if num == 0:
        return ''
    return dec_to_cus(num//36) + numbers[num % 36]


numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
arr = [[0] * 50 for _ in range(36)]
for _ in range(n):
    num = list(reversed(input()))
    for i in range(len(num)):
        arr[numbers.index(num[i])][i] += 1
k = int(input())
answer = 0
check = [0] * 35
for j in range(36):
    tmp = 0
    for i in range(50):
        if arr[j][i] > 0:
            answer += 36 ** i * j * arr[j][i]
            if j < 35:
                tmp += 36 ** i * (35 - j) * arr[j][i]
    if j < 35:
        check[j] = tmp
check.sort(reverse=True)
answer += sum(check[:k])
if answer == 0:
    print(0)
else:
    answer = dec_to_cus(answer)
    print(answer)