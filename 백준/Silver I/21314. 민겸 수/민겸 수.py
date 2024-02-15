string = input()
max_ans = ''
m_cnt = 0
min_ans = ''
for char in string:
    if char == 'M':
        if m_cnt == 0:
            min_ans += '1'
        m_cnt += 1
    else:
        if m_cnt:
            min_ans += '0' * (m_cnt - 1)
        min_ans += '5'
        max_ans += '5' + '0' * m_cnt
        m_cnt = 0
if m_cnt:
    min_ans += '0' * (m_cnt - 1)
    max_ans += '1' * m_cnt
print(max_ans)
print(min_ans)