n, k = map(int, input().split())
durability = list(map(int, input().split()))
dura_start = 0
robot = [False] * 2 * n
robot_start = 0
broken = 0
answer = 0
while broken < k:
    answer += 1
    dura_start = (dura_start - 1) % (2 * n)
    robot_start = (robot_start - 1) % (2 * n)
    if robot[(robot_start + n - 1) % (2 * n)]:
        robot[(robot_start + n - 1) % (2 * n)] = False
    for i in range(robot_start + n - 1, robot_start - 1, -1):
        i %= 2 * n
        if robot[i] and durability[(i + 1) % (2 * n)] and not robot[(i + 1) % (2 * n)]:
            robot[i] = False
            robot[(i + 1) % (2 * n)] = True
            durability[(i + 1) % (2 * n)] -= 1
            if durability[(i + 1) % (2 * n)] == 0:
                broken += 1
    if robot[(robot_start + n - 1) % (2 * n)]:
        robot[(robot_start + n - 1) % (2 * n)] = False
    if durability[robot_start]:
        durability[robot_start] -= 1
        if durability[robot_start] == 0:
            broken += 1
        robot[robot_start] = True
print(answer)