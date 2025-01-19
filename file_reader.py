def read_sudoku(file_path):
    sudoku = []
    with open(file_path, 'r') as f:
        for row in f:
            temp = row.split()
            sudoku.append([int(c) for c in temp])
    return sudoku

def print_sudoku(sudoku):
    for row in sudoku:
        print(" ".join(str(num) for num in row))
