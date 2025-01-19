# Genetic Sudoku Solver

A Python Sudoku puzzle solver using a Genetic Algorithm.

## Overview

This project implements a Genetic Algorithm to solve Sudoku puzzles. Genetic Algorithms are a type of evolutionary algorithm inspired by natural selection, and they are particularly effective for optimization problems like Sudoku. This solver demonstrates how computational intelligence can tackle challenging puzzles with elegance and efficiency.

## Features

- **Algorithm Design**: Utilizes a Genetic Algorithm to evolve potential solutions iteratively.
- **Flexible Input**: Accepts Sudoku puzzles of various difficulty levels.
- **Performance-Oriented**: Designed to find solutions in a reasonable timeframe while demonstrating the principles of Genetic Algorithms.

## Requirements

- Python 3.0 (at least)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Genetic-Sudoku-Solver.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Genetic-Sudoku-Solver
   ```

3. (Optional) Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. Install required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script to solve a Sudoku puzzle:

```bash
python3 main.py
```

### Input Format

The Sudoku puzzle should be provided in the script as a 9x9 grid, where:
- `0` represents an empty cell.
- Non-zero digits represent pre-filled cells.

Example:
```python
puzzle = [
7 8 0 4 0 0 1 2 0
6 0 0 0 7 5 0 0 9
0 0 0 6 0 1 0 7 8
0 0 7 0 4 0 2 6 0
0 0 1 0 5 0 9 3 0
9 0 4 0 6 0 0 0 5
0 7 0 3 0 0 0 1 2
1 2 0 0 0 7 4 0 0
0 4 9 2 0 6 0 0 7
]
```

You can modify the puzzle to suit your needs.

## How It Works

1. **Initialization**: The algorithm generates a population of random candidate solutions.
2. **Fitness Evaluation**: Each candidate solution is scored based on how closely it matches the constraints of a valid Sudoku puzzle.
3. **Selection**: The best candidates are selected to pass their "genes" (values) to the next generation.
4. **Crossover and Mutation**: New candidates are created by combining parts of the best solutions and introducing small random changes to maintain diversity.
5. **Iteration**: This process is repeated for multiple generations until a valid solution is found or a stopping criterion is met.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality, performance, or usability of this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

This project is inspired by the principles of Genetic Algorithms and their application to optimization problems. Special thanks to the open-source community for providing tools and frameworks that made this project possible.

---

Happy solving! If you find this project useful, don't forget to give it a star! ⭐



![Screenshot from 2025-01-19 13-10-34](https://github.com/user-attachments/assets/5b017696-596d-48d5-b331-3c72a3e3898f)
![Figure_1](https://github.com/user-attachments/assets/0a32e5e0-af37-4b7b-a156-79dc824106a7)

