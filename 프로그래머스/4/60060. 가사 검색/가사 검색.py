def solution(words, queries):
    answer = []
    l = len(words)
    right_mark = sorted(words, key=lambda x:(len(x), x))
    left_mark = sorted(map(lambda x:''.join(reversed(x)), words), key=lambda x:(len(x), x))
    for q in queries:
        if q[0] == '?':
            q_len = len(q)
            left_word = ''.join(reversed(q)).replace('?', 'a')
            right_word = ''.join(reversed(q)).replace('?', 'z')
            s = 0
            e = l - 1
            while s <= e:
                mid = (s + e) // 2
                now_word = left_mark[mid]
                if len(now_word) > q_len:
                    e = mid - 1
                elif len(now_word) < q_len:
                    s = mid + 1
                else:
                    if now_word >= left_word:
                        e = mid - 1
                    else:
                        s = mid + 1
            left_idx = e
            s = 0
            e = l - 1
            while s <= e:
                mid = (s + e) // 2
                now_word = left_mark[mid]
                if len(now_word) > q_len:
                    e = mid - 1
                elif len(now_word) < q_len:
                    s = mid + 1
                else:
                    if now_word >= right_word:
                        e = mid - 1
                    else:
                        s = mid + 1
            right_idx = e
            answer.append(right_idx - left_idx)
        else:
            q_len = len(q)
            left_word = q.replace('?', 'a')
            right_word = q.replace('?', 'z')
            s = 0
            e = l - 1
            while s <= e:
                mid = (s + e) // 2
                now_word = right_mark[mid]
                if len(now_word) > q_len:
                    e = mid - 1
                elif len(now_word) < q_len:
                    s = mid + 1
                else:
                    if now_word >= left_word:
                        e = mid - 1
                    else:
                        s = mid + 1
            left_idx = e
            s = 0
            e = l - 1
            while s <= e:
                mid = (s + e) // 2
                now_word = right_mark[mid]
                if len(now_word) > q_len:
                    e = mid - 1
                elif len(now_word) < q_len:
                    s = mid + 1
                else:
                    if now_word >= right_word:
                        e = mid - 1
                    else:
                        s = mid + 1
            right_idx = e
            answer.append(right_idx - left_idx)
    return answer