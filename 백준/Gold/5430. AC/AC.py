from collections import deque
T = int(input())
for _ in range(T):
    commands = list(map(lambda x: x, input()))
    N = int(input())
    M = 0
    nums = deque(eval(input()))
    for command in commands:
        if command == 'D':
            M += 1
    if M > N:
        print('error')
        continue
    elif M == N:
        print('[]')
        continue
    index = True
    for command in commands:
        if command == 'R':
            if index:
                index = False
            else:
                index = True
        else:
            if index:
                nums.popleft()
            else:
                nums.pop()
    if not index:
        nums.reverse()
    print(str(list(nums)).replace(' ', ''))