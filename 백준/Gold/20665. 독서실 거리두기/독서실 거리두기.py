import sys
input = sys.stdin.readline

def time_idx_change(time):
    time -= 900
    idx = 1
    idx += (time // 100) * 60
    idx += time % 100
    return idx


def check_room(number, time):
    check = 0
    while time > 0:
        check += ssum[number][time]
        time -= time & -time
    return check


def make_room(number, time, inout):
    while time <= 720:
        ssum[number][time] += inout
        time += time & -time


n, t, p = map(int, input().split())
books = sorted(tuple(map(int, input().split())) for _ in range(t))
answer = 720
ssum = [[0] * 722 for _ in range(n)]
rooms = []
for come, out in books:
    new_rooms = []
    come = time_idx_change(come)
    out = time_idx_change(out)
    for room_num in rooms:
        if check_room(room_num, come):
            new_rooms.append(room_num)
    idx = 0
    if new_rooms:
        last = -1
        gap = 0
        for room in new_rooms:
            if last == -1:
                if room > 0:
                    gap = room
            if (room - last) // 2 > gap:
                gap = (room - last) // 2
                idx = last + gap
            last = room
        if (n - 1 - last) > gap:
            idx = n - 1
    make_room(idx, come, 1)
    make_room(idx, out, -1)
    if idx == p - 1:
        answer -= out - come
    new_rooms.append(idx)
    rooms = sorted(new_rooms)
print(answer)