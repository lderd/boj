dp = [3000000] * 13
cnt = 0
for button in map(int, input().split()):
    if button == 0:
        break
    tmp = [3000000] * 13
    cnt += 1
    button -= 1
    if cnt == 1:
        tmp[1 << button] = 2
    else:
        for i in range(1, 13):
            if dp[i] < 3000000:
                # 이미 발판 위에 발이 올려져 있다면
                if i & 1 << button:
                    tmp[i] = min(tmp[i], dp[i] + 1)
                else:
                    for j in range(4):
                        # 옮길 발
                        move_foot = i & 1 << j
                        if move_foot:
                            # 발이 하나만 올라가 있던 경우
                            if i == move_foot:
                                # 반대쪽이면
                                if (j + 2) % 4 == button:
                                    tmp[1 << button] = min(dp[i] + 4, tmp[1 << button])
                                # 옆이면
                                else:
                                    tmp[1 << button] = min(dp[i] + 3, tmp[1 << button])
                                # 새로 발을 올리면
                                tmp[i + (1 << button)] = min(dp[i] + 2, tmp[i + (1 << button)])
                            # 발이 둘 다 올라가 있는데
                            else:
                                # 반대쪽 발을 옮기면
                                if (j + 2) % 4 == button:
                                    tmp[i - move_foot + (1 << button)] = min(dp[i] + 4, tmp[i - move_foot + (1 << button)])
                                # 옆 발을 옮기면
                                else:
                                    tmp[i - move_foot + (1 << button)] = min(dp[i] + 3, tmp[i - move_foot + (1 << button)])
    dp = tmp
print(min(dp))