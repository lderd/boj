def sudoku(idx):
    global flag
    if idx >= l:
        flag = True
        return
    i, j = binkan[idx]
    for tmp in range(1, 10):
        if tmp not in rows[i] and tmp not in cols[j] and tmp not in kan[i//3*3+j//3]:
            rows[i].add(tmp)
            cols[j].add(tmp)
            kan[i//3*3+j//3].add(tmp)
            puzzle[i][j] = tmp
            sudoku(idx+1)
            if flag:
                return
            rows[i].remove(tmp)
            cols[j].remove(tmp)
            kan[i//3*3+j//3].remove(tmp)



puzzle = [list(map(int, input())) for _ in range(9)]
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
kan = [set() for _ in range(9)]
binkan = []
for i in range(9):
    for j in range(9):
        tmp = puzzle[i][j]
        if tmp == 0:
            binkan.append((i, j))
        else:
            rows[i].add(tmp)
            cols[j].add(tmp)
            kan[i//3*3+j//3].add(tmp)
l = len(binkan)
flag = False
sudoku(0)
for i in range(9):
    for j in range(9):
        print(puzzle[i][j], end='')
    print()