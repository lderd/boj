n = int(input()[:-2] + '00')
f = int(input())
answer = str((f - n % f) % f)
if len(answer) == 1:
    print('0' + answer)
else:
    print(answer)