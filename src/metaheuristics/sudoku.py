import numpy as np

def measure_error(matrix):
    total_error = 0
    for row in matrix:
        row_uniq = np.unique(row.flatten())
        total_error += 9 - len(row_uniq[row_uniq != 0])
    for col in matrix.transpose():
        col_uniq = np.unique(col.flatten())
        total_error += 9 - len(col_uniq[col_uniq != 0])
    for i in [0,3,6]:
        for j in [0,3,6]:
            cell = matrix[i:i+3,j:j+3]
            cell_uniq = np.unique(cell.flatten())
            total_error += 9 - len(cell_uniq[cell_uniq != 0])
    return total_error

def get_problem(base=3):
    side  = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s))
    rBase = range(base)
    rows  = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols  = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [[nums[pattern(r,c)] for c in cols] for r in rows]

    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0
    return np.array(board)
