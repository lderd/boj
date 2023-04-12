def 풀이(sentence):
    tag = ''
    word = ''
    tag_open = False
    answer = ''
    for char in sentence:
        if char == '<':
            answer += 뒤집기(word)
            word = ''
            tag_open = True
        elif char == '>':
            tag += '>'
            tag_open = False
            answer += tag
            tag = ''
        if tag_open:
            tag += char
        else:
            if char == '>':
                continue
            if char == ' ':
                answer += 뒤집기(word) + ' '
                word = ''
            else:
                word += char
    answer += 뒤집기(word)
    return answer


def 뒤집기(word):
    tmp = ''
    for char in word:
        tmp = char + tmp
    return tmp


sentence = input()
print(풀이(sentence))