a = input()
b = input()
lena = len(a)
lenb = len(b)
a = '0' * lenb + a + '0' * lenb
answer = lena + lenb
for i in range(lena+lenb):
    tmp = 0
    for j in range(len(a)):
        if i <= j < i+lenb:
            if a[j] == b[j-i] == '2':
                break
        if a[j] != '0' or i <= j < i+lenb:
            tmp += 1
        if tmp >= answer:
            break
    else:
        answer = tmp
print(answer)