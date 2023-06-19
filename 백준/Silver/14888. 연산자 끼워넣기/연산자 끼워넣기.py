import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
arr = list(map(int, input().split()))


operand = []
for i in range(4):
    if i == 0:
        for j in range(arr[i]):
            operand.append('+')


    elif i == 1:
        for j in range(arr[i]):
            operand.append('-')

    elif i == 2:
        for j in range(arr[i]):
            operand.append('*')


    else:
        for j in range(arr[i]):
            operand.append('/')


# print(operand)


visited = [0] * (n - 1)
minn = 10 ** 10
maxx = -(10 ** 10)

def dfs(L, check):
    global maxx
    global minn

    if L == n - 1:
        # print('check', check)
        if check >= maxx:
            maxx = check

        if check <= minn:
            minn = check
        check = num[0]
        # print('maxx, minn', maxx, minn)
        # print('======끝=======')
        return (maxx, minn)

        minn = 10 ** 10
        maxx = - (10 ** 10)

    else:
        #operand갯수만큼
        for i in range(n - 1):
            # print(i)
            if visited[i] == 0:
                if operand[i] == '+':
                    # print(check, end=' ')
                    Ncheck = check + num[L + 1]
                    # print('+', num[L + 1], '=', check)

                elif operand[i] == '-':
                    # print(check, end=' ')
                    Ncheck = check - num[L + 1]
                    # print('-', num[L + 1], '=', check)

                elif operand[i] == '*':
                    # print(check, end=' ')
                    Ncheck = check * num[L + 1]
                    # print('*', num[L + 1], '=', check)

                else:
                    if check >= 0:
                        # print(check, end=' ')
                        Ncheck = check // num[L + 1]
                        # print('//', num[L + 1], '=', check)

                    else:
                        Ncheck = -((check * -1) // num[L + 1])


                # print(result)
                visited[i] = 1
                # print('[check b4 dfs]', check)
                dfs(L + 1, Ncheck)
                visited[i] = 0
                Ncheck = check


dfs(0, num[0])
print(maxx)
print(minn)