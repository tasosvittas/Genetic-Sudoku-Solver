from file_reader import print_sudoku
import matplotlib.pyplot as plt
import random as rnd

GRID_SIZE = 9
SUBGRID_SIZE = 3

#gonidio rand 9 & shuffle 
def make_gene(initial_row):
    mapp = {}
    gene = list(range(1, 10))
    rnd.shuffle(gene)
    for i in range(GRID_SIZE):
        mapp[gene[i]] = i
    for i in range(GRID_SIZE):
        if initial_row[i] != 0 and gene[i] != initial_row[i]:
            temp = gene[i], gene[mapp[initial_row[i]]]
            gene[mapp[initial_row[i]]], gene[i] = temp
            mapp[initial_row[i]], mapp[temp[0]] = i, mapp[initial_row[i]]
    return gene

def make_chromosome(initial_sudoku):
    chromosome = []
    for row in initial_sudoku:
        chromosome.append(make_gene(row))
    return chromosome

#orizw ti plythismo chromosomes thelw na eksetazei
def make_population(population_size, initial_sudoku):
    population = []
    for _ in range(population_size):
        population.append(make_chromosome(initial_sudoku))
    return population

def fitness(chromosome):
    score = 0
    # gia kathe grammi 9 * 9 = 81
    score += sum(len(set(row)) for row in chromosome)
    # gia kathe stili 9 * 9 = 81
    score += sum(len(set(chromosome[row][col] for row in range(len(chromosome))))
                 for col in range(len(chromosome)))
    # gia kathe block 9 * 9 = 81
    subgrid_size = int(len(chromosome) ** 0.5)
    for block_row in range(0, len(chromosome), subgrid_size):
        for block_col in range(0, len(chromosome), subgrid_size):
            subgrid = [chromosome[r][c]
                       for r in range(block_row, block_row + subgrid_size)
                       for c in range(block_col, block_col + subgrid_size)]
            score += len(set(subgrid))
    #ara to veltisto score tha einai 81 + 81 + 81 = 243
    return score

def select(population):
    #to kalytero chromosome metaksy enws sample 3wn
    tournament = rnd.sample(population, 5)
    return max(tournament, key=fitness)
    
def crossover(parent1, parent2):
    child1, child2 = [], []
    #epilogi grammis 50% pithanotithta 1 or 2 gonea
    for i in range(GRID_SIZE):
        if rnd.random() > 0.5:
            child1.append(parent1[i])
            child2.append(parent2[i])
        else:
            child1.append(parent2[i])
            child2.append(parent1[i])
    return child1, child2


def mutation(chromosome, mutation_rate, initial_sudoku):
    for i in range(9):
        x = rnd.randint(0, 100)
        if x < mutation_rate * 100:
            chromosome[i] = make_gene(initial_sudoku[i])
    return chromosome

def is_solution(chromosome):
    return fitness(chromosome) == 243  # 81+81+81=243

def plot_progress(generations, best_fitness_scores, avg_fitness_scores):
    plt.plot(generations, best_fitness_scores, label="Best Fitness")
    plt.plot(generations, avg_fitness_scores, label="Average Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.title("Genetic Algorithm Progress")
    plt.show()

# def genetic_algorithm(initial_sudoku, population_size=200, generations=30000, mutation_rate=0.1):
#     population = make_population(population_size, initial_sudoku)
#     best_fitness_scores = []
#     avg_fitness_scores = []
#     generation_list = []

#     for generation in range(generations):
#         # ypologismos gia plot kai print
#         population = sorted(population, key=fitness, reverse=True)
#         best_fitness = fitness(population[0])
#         avg_fitness = sum(fitness(ind) for ind in population) / population_size

#         best_fitness_scores.append(best_fitness)
#         avg_fitness_scores.append(avg_fitness)
#         generation_list.append(generation)

#         print(f"Generation {generation}, Best Fitness: {best_fitness}")
        
#         # to kalytero sudoku
#         print("Best Sudoku:")
#         print_sudoku(population[0])
#         print("-" * 30)

#         # elegxos gia solution
#         if is_solution(population[0]):
#             print(f"Solution found in generation {generation}!")
#             plot_progress(generation_list, best_fitness_scores, avg_fitness_scores)
#             return population[0]

#         #next generation
#         next_population = population[:5]  # Elitismos: diathrw tis 5 kalyteres lyseis
#         while len(next_population) < population_size:
#             parent1 = select(population)
#             parent2 = select(population)
#             child1, child2 = crossover(parent1, parent2)
#             child1 = mutation(child1, mutation_rate, initial_sudoku)
#             child2 = mutation(child2, mutation_rate, initial_sudoku)
#             next_population.extend([child1, child2])
#         population = next_population[:population_size]

#     plot_progress(generation_list, best_fitness_scores, avg_fitness_scores)
#     print("No solution found within the generation limit.")
#     return None

def genetic_algorithm(initial_sudoku, population_size=200, generations=30000, mutation_rate=0.1):
    population = make_population(population_size, initial_sudoku)
    best_fitness_scores = []
    avg_fitness_scores = []
    generation_list = []

    for generation in range(generations):
        # Calculate fitness for plotting and printing
        population = sorted(population, key=fitness, reverse=True)
        best_fitness = fitness(population[0])
        avg_fitness = sum(fitness(ind) for ind in population) / population_size

        best_fitness_scores.append(best_fitness)
        avg_fitness_scores.append(avg_fitness)
        generation_list.append(generation)

        print(f"Generation {generation}, Best Fitness: {best_fitness}")
        print("Best Sudoku:")
        print_sudoku(population[0])
        print("-" * 30)

        # Check if solution is found
        if is_solution(population[0]):
            print(f"Solution found in generation {generation}!")
            plot_progress(generation_list, best_fitness_scores, avg_fitness_scores)
            return population[0]

        # Create the next generation
        next_population = population[:10]  # Elitism: Keep the top 10 individuals

        # Crossover and mutation for the rest of the population
        while len(next_population) < population_size:
            parent1 = select(population)
            parent2 = select(population)
            child1, child2 = crossover(parent1, parent2)

            # Apply mutation with adaptive probabilities
            child1 = mutation(child1, mutation_rate, initial_sudoku)
            child2 = mutation(child2, mutation_rate, initial_sudoku)

            next_population.extend([child1, child2])

        # Apply forced mutation on a small fraction of the weakest individuals
        weakest_start = int(0.8 * population_size)
        for i in range(weakest_start, population_size):
            next_population[i] = mutation(next_population[i], mutation_rate * 1.5, initial_sudoku)

        population = next_population[:population_size]

    plot_progress(generation_list, best_fitness_scores, avg_fitness_scores)
    print("No solution found within the generation limit.")
    return None
