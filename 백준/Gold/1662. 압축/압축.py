code = input()
length = len(code)

formula = ''
tmp = 0

i = 0
while i < length:
    if code[i].isdigit():
        if i == length - 1:
            formula += f'+{tmp+1}'
        elif code[i+1] == '(':
            formula += f'+{tmp}+{code[i]}*('
            tmp = 0
        else:
            tmp += 1
    elif code[i] == ')':
        formula += f'+{tmp})'
        tmp = 0

    i += 1
print(eval(formula))