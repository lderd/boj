t = int(input())
for _ in range(t):
    string = input()
    i = 0
    j = len(string) - 1
    answer = 2
    flag = 0

    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            if flag == 1:
                break
            if string[i+1] == string[j]:
                i += 1
                flag = 1
            else:
                break
    if i >= j:
        answer = 0
        if flag == 1:
            answer = 1

    if answer == 2:
        flag = 0
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                if flag == 1:
                    break
                if string[i] == string[j-1]:
                    j -= 1
                    flag = 1
                else:
                    break
        if i >= j:
            answer = 0
            if flag == 1:
                answer = 1
    print(answer)