n = int(input())
arr = [True] * (n + 1)
for i in range(2, n // 2 + 1):
    tmp = i + i
    while tmp <= n:
        arr[tmp] = False
        tmp += i
able = set()
disable = set()
for i in range(7, n+1):
    if arr[i]:
        num = i
        tmp_set = set()
        flag = 0
        while True:
            if num == 1:
                print(i)
                flag = 1
                break
            tmp_set.add(num)
            num = sum(map(lambda x: int(x) ** 2, str(num)))
            if num in able:
                print(i)
                flag = 1
                break
            elif num in disable:
                break
            elif num in tmp_set:
                break
        if flag:
            able |= tmp_set
        else:
            disable |= tmp_set