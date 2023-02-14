n = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))
arrC = sorted(arrA)
index = n-1
while index > 0:
    if arrA[index] == arrB[index] == arrC[index]:
        index -= 1
    elif arrA[index] != arrB[index] == arrC[index]:
        for i in range(index):
            if arrA[i] > arrA[i+1]:
                arrA[i], arrA[i+1] = arrA[i+1], arrA[i]
        index -= 1
    elif arrB[index] != arrC[index]:
        break
answer = 0
if arrA == arrB:
    answer = 1
else:
    for i in range(index):
        if arrA[i] > arrA[i+1]:
            arrA[i], arrA[i+1] = arrA[i+1], arrA[i]
        if arrA == arrB:
            answer = 1
            break
print(answer)