from functools import cmp_to_key
def solution(N, stages):
    def cmp(a, b):
        a_user, a_pass, a_stage = a
        b_user, b_pass, b_stage = b
        if a_user == 0:
            a_rate = 0
        elif b_pass == 0:
            a_rate = a_user
        else:
            a_rate = a_user * b_pass
        if b_user == 0:
            b_rate = 0
        elif a_pass == 0:
            b_rate = b_user
        else:
            b_rate = b_user * a_pass
        if a_rate == b_rate:
            return a_stage - b_stage
        else:
            return b_rate - a_rate
    answer = []
    users = sorted(stages)
    total = len(users)
    rate = []

    now_stage = 1
    now_users = 0
    before_users = 0
    idx = 0
    while now_stage <= N:
        while idx < total and users[idx] <= now_stage:
            now_users += 1
            idx += 1
        rate.append((now_users, total - before_users, now_stage))
        now_stage += 1
        before_users += now_users
        now_users = 0
    rate.sort(key=cmp_to_key(cmp))
    for *_, stage in rate:
        answer.append(stage)
    return answer