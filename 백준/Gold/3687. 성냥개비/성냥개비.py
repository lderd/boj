t = int(input())
a = {2:'1', 3:'7', 4:'4', 5:'2', 6:'6', 7:'8', 8:'10', 9:'18', 10:'22', 11:'20', 12:'00', 13:'68', 14:'88'}
aa = {2:['1'], 3:['7'], 4:['4'], 5:['2'], 6:['6'], 7:['8'], 8:['1', '0'], 9:['1', '8'], 10:['2', '2'], 11:['2', '0'], 12:['2', '8'], 13:['6', '8'], 14:['8', '8']}
small = [''] * 101
for i in range(2, 15):
    small[i] = ''.join(aa[i])
for i in range(15, 101):
    for j in range(2, 15):
        if i - j >= 2:
            tmp = sorted(list(small[i-j] + a[j]))
            for k in range(len(tmp)):
                if tmp[k] != '0':
                    tmp[0], tmp[k] = tmp[k], tmp[0]
                    break
            tmp = ''.join(tmp)
            if small[i]:
                if int(small[i]) > int(tmp):
                    small[i] = tmp
            else:
                small[i] = tmp


for _ in range(t):
    n = int(input())
    big = ''
    big_cnt = n
    while big_cnt > 0:
        if big_cnt == 3:
            big = '7' + big
            big_cnt -= 3
        else:
            big += '1'
            big_cnt -= 2
    print(small[n], big)