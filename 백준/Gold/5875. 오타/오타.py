a = input()
plus = a.count('(')
minus = a.count(')')
pplus = 0
mminus = 0
if -1 <= plus - minus <= 1:
    print(0)
elif plus > minus:
    for i in range(plus + minus):
        if a[-i-1] == '(':
            pplus += 1
        else:
            mminus += 1
        if mminus < pplus:
            print(pplus)
            break
else:
    for i in range(plus + minus):
        if a[i] == '(':
            pplus += 1
        else:
            mminus += 1
        if mminus > pplus:
            print(mminus)
            break
