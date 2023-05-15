a = int(input())
b = int(input())
c = int(input())
cnt = 0
if a == b:
    cnt += 1
if a == c:
    cnt += 1
if b == c:
    cnt += 1
if a + b + c == 180:
    if cnt == 3:
        print('Equilateral')
    elif cnt == 1:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')