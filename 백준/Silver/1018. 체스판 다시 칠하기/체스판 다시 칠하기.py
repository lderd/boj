# 세로, 가로
def Greed():
    cnt = 64
    for i in range(M-7):
        for j in range(N-7):
            tmp1 = 0
            tmp2 = 0
            flag = 0
            for ii in range(8):
                for jj in range(8):
                    if arr[i+ii][j+jj] != standard1[ii][jj]:
                        tmp1 += 1
                    if arr[i+ii][j+jj] != standard2[ii][jj]:
                        tmp2 += 1
                    if tmp1 >= cnt and tmp2 >= cnt:
                        flag = 1
                        break
                if flag == 1:
                    break
            cnt = min(tmp1, tmp2)
    return cnt


M, N = map(int, input().split())
arr = [input() for _ in range(M)]
standard1 = ['WB' * 4, 'BW' * 4] * 4
standard2 = ['BW' * 4, 'WB' * 4] * 4
result = Greed()
print(result)