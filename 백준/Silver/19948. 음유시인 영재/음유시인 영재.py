poem = input()
space = int(input())
cnt = list(map(int, input().split()))
last = 0
answer = -1
for char in poem:
    char = ord(char)
    if char != last:
        if char == 32:
            if space:
                space -= 1
            else:
                break
        elif 65 <= char <= 90:
            if cnt[char-65]:
                cnt[char-65] -= 1
            else:
                break
        else:
            if cnt[char-97]:
                cnt[char-97] -= 1
            else:
                break
    last = char
else:
    answer = ''.join(map(lambda x:x[0].upper(), poem.split()))
    last = 0
    for char in answer:
        char = ord(char)
        if char != last:
            if char == 32:
                if space:
                    space -= 1
                else:
                    answer = -1
                    break
            elif 65 <= char <= 90:
                if cnt[char - 65]:
                    cnt[char - 65] -= 1
                else:
                    answer = -1
                    break
            else:
                if cnt[char - 97]:
                    cnt[char - 97] -= 1
                else:
                    answer = -1
                    break
        last = char
print(answer)