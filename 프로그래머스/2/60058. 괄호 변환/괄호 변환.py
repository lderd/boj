def solution(p):
    def dfs(w):
        if w == '':
            return ''
        bracket_open = 0
        bracket_close = 0
        flag = True
        for char in w:
            if char == '(':
                bracket_open += 1
            else:
                bracket_close += 1
            if bracket_open == bracket_close:
                break
            if bracket_close > bracket_open:
                flag = False
        u = w[:bracket_open+bracket_close]
        v = w[bracket_open+bracket_close:]
        # u가 올바른 괄호 문자열이라면
        if flag:
            return u + dfs(v)
        else:
            ul = len(u)
            new_u = ''
            for i in range(1, ul-1):
                new_u += '(' if u[i] == ')' else ')'
            return '(' + dfs(v) + ')' + new_u
    answer = dfs(p)
    return answer