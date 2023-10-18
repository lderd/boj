from itertools import permutations
def solution(n, weak, dist):
    dist_ = list(set(permutations(dist, len(dist))))
    weak_ = weak + list(map(lambda x: x+n, weak))
    answer = len(dist) + 1
    # 친구 조합중에 하나
    for friends in dist_:
        for j in range(len(weak)):
            weak_points = weak_[j:j+len(weak)]
            tmp = 0
            tmp_endpoint = weak_points[0] + friends[tmp]
            for k in weak_points:
                if tmp + 1 >= answer:
                    break
                if tmp_endpoint >= k:
                    continue
                else:
                    if tmp < len(friends) - 1:
                        tmp += 1
                        tmp_endpoint = k + friends[tmp]
                    else:
                        break
            else:
                answer = tmp + 1
    if answer == len(dist) + 1:
        return -1
    else:
        return answer