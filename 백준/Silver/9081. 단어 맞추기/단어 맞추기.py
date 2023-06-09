n = int(input())
for _ in range(n):
    word = list(input())
    new_word = []
    for i in range(len(word)-2, -1, -1):
        tmp = -1
        for j in range(i + 1, len(word)):
            if word[i] < word[j] and (tmp == -1 or word[tmp] > word[j]):
                tmp = j
        if tmp > -1:
            new_word = word[:i] + [word[tmp]] + sorted(word[i:tmp] + word[tmp + 1:])
            break
    if new_word:
        print(''.join(new_word))
    else:
        print(''.join(word))