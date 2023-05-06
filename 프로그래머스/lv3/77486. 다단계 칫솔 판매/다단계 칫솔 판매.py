from collections import defaultdict
def solution(enroll, referral, seller, amount):
    def 판매금분배(나, 금액):
        분배금 = 금액 // 10
        if 분배금 > 0:
            if 추천인[나] != -1:
                판매금분배(추천인[나], 분배금)
        answer[나] += 금액 - 분배금


    사람수 = len(enroll)
    answer = [0] * 사람수
    내순서 = defaultdict(int)
    추천인 = defaultdict(int)
    for i in range(사람수):
        if referral[i] == '-':
            추천인[i] = -1
        else:
            추천인[i] = enroll.index(referral[i])
        내순서[enroll[i]] = i
    for i in range(len(seller)):
        판매금분배(내순서[seller[i]], amount[i] * 100)
    return answer