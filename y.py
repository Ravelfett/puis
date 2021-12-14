import random

def show(board):
    r = ""
    for i in range(6):
        for j in board:
            for k in range(len(j)):
                if i == k:
                    if j[k] == 0:
                        r += "  "
                    elif j[k] == 1:
                        r += "\033[1;31;40m" + "X " + "\033[0m"
                    elif j[k] == -1:
                        r += "\033[1;34;40m" + "O " + "\033[0m"
        print("|"+r+"|")
        r = ""
    print("\x1b[6;30;42m" + "|"+" ".join([str(i) for i in range(7)])+" |" + "\x1b[0m")


def top(board, row):
    index = -1
    if row < 0 or row > 6:
        return index
    for i in board[row]:
        if i != 0:
            return index
        index += 1
    return index

def play(board, row, v):
    o = top(board, row)
    if o >= 0:
        board[row][o] = v
        return True
    return False

def count(board, px, py, vx, vy, v):
    c = 0
    m = 0
    px -= vx
    py -= vy
    while px+vx in range(7) and py+vy in range(6):
        px += vx
        py += vy
        if board[px][py] == v:
            c += 1
            m = max(m, c)
        else:
            c = 0
    m = max(m, c)
    return m

def check(board, v):
    m = 0
    for i in range(7):
        c = count(board, i, 0, 0, 1, v)
        m = max(m, c)
    for i in range(6):
        c = count(board, 0, i, 1, 0, v)
        m = max(m, c)
    for i in range(7):
        c = count(board, i, 0, 1, 1, v)
        m = max(m, c)
        c = count(board, i, 0, -1, 1, v)
        m = max(m, c)
    for i in range(6):
        c = count(board, 0, i, 1, 1, v)
        m = max(m, c)
    for i in range(6):
        c = count(board, 6, i, -1, 1, v)
        m = max(m, c)
    return m

def minmax(board, v, g, d):
    if check(board, v) >= 4:
        if v == g:
            return 1, 0
        else:
            return -1, 0
    if d == 0:
        return 0, 0
    moves = []
    for i in range(7):
        cpboard = [i[:] for i in board]
        if play(cpboard, i, v):
            moves.append([i, minmax(cpboard, -v, g, d-1)[0]])
    if len(moves)==0:
        return 0, 0
    o = 0
    for i in moves:
        o+=i[1]
    c = []
    m = moves[0][1]
    for i in moves:
        if v == g:
            if i[1]>m:
                m = i[1]
        else:
            if i[1]<m:
                m = i[1]
    for i in moves:
        if i[1] == m:
            c.append(i[0])
    if d == 5:
        print(moves)
    if m == 1 or m == -1:
        return m, random.choice(c)
    return o/7, random.choice(c)



board = [[0 for j in range(6)] for i in range(7)]
player = 1
playing = True

while playing:
    show(board)
    p = "X"
    if player == -1:
        p = "O"
    if player == -1:
        inp = str(minmax(board, player, player, 5)[1])
    else:
        inp = input(p+" > ")
        #inp = str(minmax(board, player, player, 5)[1])
    if inp.isnumeric():
        if play(board, int(inp), player):
            if check(board, player) >= 4:
                show(board)
                print("GAñ222222222222")
                playing = False
            player = -player
