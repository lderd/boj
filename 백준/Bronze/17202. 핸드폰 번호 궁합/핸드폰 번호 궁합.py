a = input()
b = input()
answer = []
for i in range(8):
    answer.append(int(a[i]))
    answer.append(int(b[i]))
for cnt in range(16, 2, -1):
    tmp = []
    for i in range(cnt-1):
        tmp.append((answer[i] + answer[i+1]) % 10)
    answer = tmp
print(f'{answer[0]}{answer[1]}')