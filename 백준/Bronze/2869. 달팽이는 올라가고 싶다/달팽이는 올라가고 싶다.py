A, B, V = map(int, input().split())
if A == B:
    if A == V:
        print(1)
else:
    day = (V - A) / (A - B)
    if day > int(day):
        day += 2
    else:
        day += 1
    day = int(day)
    print(day)