from collections import deque
formular = deque(list(input()))
q = deque()
operator = {'+' : 0, '-' : 0, '*' : 1, '/': 1, '(' : -2, ')' : -2}
answer = ''
while formular:
    char = formular.popleft()
    if char in operator.keys():
        if q:
            if abs(operator[q[-1]]) < abs(operator[char]):
                if char == ')':
                    while q:
                        if operator[q[-1]] > operator[char]:
                            answer += q.pop()
                        else:
                            q.pop()
                            break
                else:
                    q.append(char)
            else:
                if operator[char] > -2:
                    while q:
                        if operator[q[-1]] >= operator[char]:
                            answer += q.pop()
                        else:
                            break
                q.append(char)
        else:
            q.append(char)
    else:
        answer += char
while q:
    char = q.pop()
    if operator[char] > -2:
        answer += char
print(answer)