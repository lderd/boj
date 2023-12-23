def solution(spell, dic):
    answer = 2
    spell_len = len(spell)
    for word in dic:
        for char in spell:
            if char not in word:
                break
        else:
            if len(word) == spell_len:
                answer = 1
                break
    return answer