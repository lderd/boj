from math import gcd
from bisect import bisect_right
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
balloons = []
angle = tuple()
for _ in range(N):
    x, y, hp = map(int, input().split())
    balloons.append(hp)
    gcd_ = gcd(x, y)
    angle = (x//gcd_, y//gcd_)
balloons.sort()
damage = 0
answer = N
for _ in range(M):
    if answer == 0:
        print(0)
        continue
    x, y, d = map(int, input().split())
    attack_angle = tuple()
    gcd_ = gcd(x, y)
    attack_angle = (x//gcd_, y//gcd_)
    if attack_angle == angle:
        damage += d
    answer = N - bisect_right(balloons, damage)
    print(answer)