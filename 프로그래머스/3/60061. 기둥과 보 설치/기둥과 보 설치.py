def solution(n, build_frame):
    def check(x, y, a):
        if a:
            if (x, y-1, 0) in structure or (x+1, y-1, 0) in structure or ((x-1, y, 1) in structure and (x+1, y, 1) in structure):
                return True
            return False
        else:
            if y == 0 or (x-1, y, 1) in structure or (x, y, 1) in structure or (x, y-1, 0) in structure:
                return True
            return False
    answer = [[]]
    structure = set()
    for x, y, a, b in build_frame:
#         설치
        if b:
#            보
            if a:
                if check(x, y, a):
                    structure.add((x, y, a))
#             기둥
            else:
                if check(x, y, a):
                    structure.add((x, y, a))
#       삭제
        else:
            structure.remove((x, y, a))
#           보
            if a:
                if (x-1, y, 1) in structure:
                    if not check(x-1, y, 1):
                        structure.add((x, y, a))
                        continue
                if (x+1, y, 1) in structure:
                    if not check(x+1, y, 1):
                        structure.add((x, y, a))
                        continue
                if (x, y, 0) in structure:
                    if not check(x, y, 0):
                        structure.add((x, y, a))
                        continue
                if (x+1, y, 0) in structure:
                    if not check(x+1, y, 0):
                        structure.add((x, y, a))
                        continue
#           기둥
            else:
                if (x-1, y+1, 1) in structure:
                    if not check(x-1, y+1, 1):
                        structure.add((x, y, a))
                        continue
                if (x, y+1, 1) in structure:
                    if not check(x, y+1, 1):
                        structure.add((x, y, a))
                        continue
                if (x, y+1, 0) in structure:
                    if not check(x, y+1, 0):
                        structure.add((x, y, a))
                        continue
    return sorted(list(structure))