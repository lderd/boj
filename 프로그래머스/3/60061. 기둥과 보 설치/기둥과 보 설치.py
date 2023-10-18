#### 6번, 18번 틀림 ####


from collections import deque
from pprint import pprint

def solution(n, build_frame):
    answer = []

    # 체크할 맵
    pillar_maps = [[0] * (n + 1) for _ in range(n)]
    beam_maps = [[0] * n for _ in range(n+1)]

    for frame in build_frame:
        # pprint(pillar_maps)
        # pprint(beam_maps)
        # print('============')
        x, y = frame[0], frame[1]
        is_pillar = not frame[2]
        is_install = frame[3]

        # 기둥을 설치하는거면
        if is_pillar and is_install:

            # 바닥이면 설치ㄱㄱ/ 바닥 아닌데 밑에 기둥있거나, 양옆에 보가 설치되있는지 확인
            if y == 0 or pillar_maps[y - 1][x] or (x > 0 and beam_maps[y][x - 1]) or (x < n and beam_maps[y][x]):
                pillar_maps[y][x] = 1


        # 보를 설치하는거면
        elif not is_pillar and is_install:
            # print(x, y)
            # 한쪽 끝이 기둥 위면 설치, 양옆에 빔이 있으면 설치
            if pillar_maps[y - 1][x] or pillar_maps[y - 1][x + 1] or (x > 0 and x < n - 1 and beam_maps[y][x - 1] and beam_maps[y][x + 1]):
                beam_maps[y][x] = 1



        # 기둥을 삭제하는거면
        if is_pillar and not is_install:

            # 기둥이 있으면
            if pillar_maps[y][x]:
                pillar_maps[y][x] = 0

                # 위에 기둥이 있고, 양옆 모두 보가 없으면 삭제못함
                if y < n - 1 and pillar_maps[y + 1][x] and not((x > 0 and beam_maps[y + 1][x - 1]) or (x < n and beam_maps[y + 1][x])):
                    pillar_maps[y][x] = 1

                # 위 양옆에 보가 있고, 그 보를 잡아줄 게 없으면 삭제못함
                elif x > 0 and y < n and not pillar_maps[y][x - 1] and beam_maps[y + 1][x - 1] and not((x > 1 and beam_maps[y + 1][x - 2]) and (x < n and beam_maps[y + 1][x])):
                    pillar_maps[y][x] = 1
                elif x < n and y < n and not pillar_maps[y][x + 1] and beam_maps[y + 1][x] and not((x > 0 and beam_maps[y + 1][x - 1]) and (x < n - 1 and beam_maps[y + 1][x + 1])):
                    pillar_maps[y][x] = 1


        # 보를 삭제하는거면:
        elif not is_pillar and not is_install:

            # 보가 있으면
            if beam_maps[y][x]:
                beam_maps[y][x] = 0

                # 양옆 각각 판단해서 기둥이 있고, 반대쪽에 받혀줄 보가 없거나 밑에 기둥이 없으면 삭제못함
                if pillar_maps[y][x] and not pillar_maps[y - 1][x] and not (x > 0 and beam_maps[y][x - 1]):
                    beam_maps[y][x] = 1

                elif pillar_maps[y][x + 1] and not pillar_maps[y - 1][x + 1] and not (x < n - 1 and beam_maps[y][x + 1]):
                    beam_maps[y][x] = 1

                # 양옆 각각 판단해서 보가 있고, 그 보를 바칠 기둥이 없으면 삭제
                elif x > 0 and beam_maps[y][x - 1] and not (pillar_maps[y - 1][x - 1] or pillar_maps[y - 1][x]):
                    beam_maps[y][x] = 1

                elif x < n - 1 and beam_maps[y][x + 1] and not (pillar_maps[y - 1][x + 1] or pillar_maps[y - 1][x + 2]):
                    beam_maps[y][x] = 1


    for i in range(n):
        for j in range(n+1):
            if pillar_maps[i][j]:
                answer.append([j, i, 0])

    for i in range(n+1):
        for j in range(n):
            if beam_maps[i][j]:
                answer.append([j, i, 1])

    answer.sort(key=lambda x : (x[0], x[1], x[2]))

    return answer