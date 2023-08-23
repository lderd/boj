n, m = map(int, input().split())
n_cnt = [0, 0]
m_cnt = [0, 0]
tmp2 = 2
tmp5 = 5
while tmp2 <= n:
    n_cnt[0] += n // tmp2
    m_cnt[0] += m // tmp2
    m_cnt[0] += (n - m) // tmp2
    tmp2 *= 2
while tmp5 <= n:
    n_cnt[1] += n // tmp5
    m_cnt[1] += m // tmp5
    m_cnt[1] += (n - m) // tmp5
    tmp5 *= 5
print(min(n_cnt[0] - m_cnt[0], n_cnt[1] - m_cnt[1]))