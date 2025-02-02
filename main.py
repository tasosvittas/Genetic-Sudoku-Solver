from file_reader import read_sudoku, print_sudoku
from genetic_algo import genetic_algorithm

file_path = "./sample_sudoku/easy.txt"
initial_sudoku = read_sudoku(file_path)
print("Initial Sudoku Puzzle:")
print_sudoku(initial_sudoku)
print("-" * 30)

solution = genetic_algorithm(initial_sudoku)
if solution:
    print("Solved Sudoku:")
    print_sudoku(solution)
else:
    print("Failed to solve the Sudoku puzzle.")
