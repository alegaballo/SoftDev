import sys
best = "A" * 1024
current = ''


def right(matrix, position):
    if position[1] + 1 < len(matrix[0]) and matrix[position[0]][position[1] + 1] != 'X':
        return True


def left(matrix, position):
    if position[1] - 1 >= 0 and matrix[position[0]][position[1] - 1] != 'X':
        return True


def up(matrix, position):
    if position[0] - 1 >= 0 and matrix[position[0] - 1][position[1]] != 'X':
        return True


def down(matrix, position):
    if position[0] + 1 < len(matrix) and matrix[position[0] + 1][position[1]] != 'X':
        return True


def get_moves(matrix, position):
    moves = []
    if right(matrix, position):
        moves.append('R')
    if up(matrix, position):
        moves.append('U')
    if left(matrix, position):
        moves.append('L')
    if down(matrix, position):
        moves.append('D')
    return moves


def make_move(position, move):
    if move == 'R':
        return position[0], position[1] + 1
    elif move == 'L':
        return position[0], position[1] - 1
    elif move == 'U':
        return position[0] - 1, position[1]
    else:
        return position[0] + 1, position[1]


def solve(matrix, position, end):
    global current
    global best
    if len(current) > len(best):
        return
    if position == end:
        if len(current) < len(best):
            best = current
    else:
        matrix[position[0]][position[1]] = 'X'
        moves = get_moves(matrix, position)
        if len(moves) == 0:
            return
        else:
            for move in moves:
                current += move
                solve(matrix, make_move(position, move), end)
                current = current[:-1]
            matrix[position[0]][position[1]] = 'C'

def filter_map(map_):
    filtered=[]
    filtered.append(list(map_[0]))

    for j in range(0, len(map_[0])):
        if map_[0][j] == 'O':
            filtered[0][j] = 'X'
        else:
            filtered[0][j] = 'C'
    for i in range(1, len(map_)):
        filtered.append(list(map_[i]))
        for j in range(0, len(map_[i])):
            if map_[i][j] == 'O' or map_[i - 1][j] == 'O':
                filtered[i][j] = 'X'
            else:
                filtered[i][j] = 'C'
    return filtered


def find_place(v, place):
    i = k = 0
    found = False
    for line in v:
        if place in line:
            for c in line:
                if c == place:
                    found = True
                    break
                else:
                    k += 1
        if not found:
            i += 1
    return i, k


f = open(sys.argv[1], 'r')
underground = [list(line.rstrip()) for line in f if line != '\n']
start = find_place(underground, 'S')
end = find_place(underground, 'E')
filtered = filter_map(underground)
solve(filtered, start,  end)
print best

