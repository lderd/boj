def solution(info, query):
    answer = []
    '''
    언어 cpp, java, python, -
    직군 backend, frontend, -
    경력 junior, senior, -
    소울푸드 chicken, pizza, -
    '''
    lan_idx = {'cpp':[0], 'java':[1], 'python':[2], '-':[0, 1, 2]}
    jik_idx = {'backend':[0], 'frontend':[1], '-':[0, 1]}
    gyu_idx = {'junior':[0], 'senior':[1], '-':[0, 1]}
    food_idx = {'chicken':[0], 'pizza':[1], '-':[0, 1]}
#     info1[언어][직군][경력][푸드][점수]
    info1 = [[[[[0] * (100001) for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    for strings in info:
        lan, jik, gyu, food, score = strings.split()
        score = int(score)
        while score <= 100000:
            info1[lan_idx[lan][0]][jik_idx[jik][0]][gyu_idx[gyu][0]][food_idx[food][0]][score] += 1
            score += score & -score
    for strings in query:
        lan, jik, gyu, food, score = strings.replace('and', '').split()
        tmp = 100000
        ans = 0
        while tmp > 0:
            for i in lan_idx[lan]:
                for j in jik_idx[jik]:
                    for k in gyu_idx[gyu]:
                        for l in food_idx[food]:
                            ans += info1[i][j][k][l][tmp]
            tmp -= tmp & -tmp
        score = int(score) - 1
        while score > 0:
            for i in lan_idx[lan]:
                for j in jik_idx[jik]:
                    for k in gyu_idx[gyu]:
                        for l in food_idx[food]:
                            ans -= info1[i][j][k][l][score]
            score -= score & -score
        answer.append(ans)
    return answer