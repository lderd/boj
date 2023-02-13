from collections import deque
brackets = deque(input())
last = ''
q = deque()
flag = 0
formula = ''

while brackets:
    char = brackets.popleft()

    if char == '(':
        if last == '':
            formula += '2'
        elif last == '(':
            formula += '*(2'
        elif last == '[':
            formula += '*(2'
        elif last == ')':
            formula += '+2'
        elif last == ']':
            formula += '+2'
        q.append('(')
        last = '('

    elif char == '[':
        if last == '':
            formula += '3'
        elif last == '(':
            formula += '*(3'
        elif last == '[':
            formula += '*(3'
        elif last == ')':
            formula += '+3'
        elif last == ']':
            formula += '+3'
        q.append('[')
        last = '['

    elif char == ')':
        if not q or q[-1] != '(':
            flag = 1
            break
        else:
            if last == ')' or last == ']':
                formula += ')'
            q.pop()
        last = ')'

    elif char == ']':
        if not q or q[-1] != '[':
            flag = 1
            break
        else:
            if last == ')' or last == ']':
                formula += ')'
            q.pop()
        last = ']'
if flag or q or brackets:
    print(0)
else:
    print(eval(formula))