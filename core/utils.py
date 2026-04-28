import copy

def heuristic(state, goal):
    pos = {}
    for i in range(3):
        for j in range(3):
            pos[goal[i][j]] = (i, j)

    d = 0
    for i in range(3):
        for j in range(3):
            v = state[i][j]
            if v != 0:
                gi, gj = pos[v]
                d += abs(i - gi) + abs(j - gj)
    return d


def find_zero(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i, j


def get_neighbors(s):
    x, y = find_zero(s)
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    res = []

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            ns = copy.deepcopy(s)
            ns[x][y], ns[nx][ny] = ns[nx][ny], ns[x][y]
            res.append(ns)

    return res