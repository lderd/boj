from itertools import permutations
from math import gcd
def solution(dots):
    answer = 0
    checked = set()
    for per in permutations(list(range(4)), 4):
        one, two, three, four = per
        if (one, two) in checked: continue
        checked.add((one, two))
        checked.add((three, four))
        x1, y1 = dots[one]
        x2, y2 = dots[two]
        x3, y3 = dots[three]
        x4, y4 = dots[four]
        dx1 = x1 - x2
        dy1 = y1 - y2
        dx2 = x3 - x4
        dy2 = y3 - y4
        g1 = gcd(dx1, dy1)
        g2 = gcd(dx2, dy2)
        dx1 //= g1
        dy1 //= g1
        dx2 //= g2
        dy2 //= g2
        if (dx1, dy1) == (dx2, dy2) or (-dx1, -dy1) == (dx2, dy2):
            answer = 1
            break
    return answer