import sys
import pygad
from scoring import score
from parser import parse, output


best, best_sol = 0, []


def fitness_func(solution, solution_idx):
    global best, best_sol

    return score(solution, problem)


def on_generation(ga):
    global best, best_sol
    ga_best_sol, ga_best, _ = ga.best_solution()

    if ga_best > best:
        best = ga_best
        best_sol = ga_best_sol

        print(best)
        output(best_sol)


filename = sys.argv[1]
problem = parse(filename)
N = len(problem[3])
ga_instance = pygad.GA(num_generations=50000,
                       sol_per_pop=100,
                       num_genes=N,
                       gene_space=[list(range(N)) for _ in range(N)],
                       mutation_num_genes=3,
                       random_mutation_min_val=0,
                       random_mutation_max_val=len(problem[3]),
                       num_parents_mating=2,
                       fitness_func=fitness_func,
                       gene_type=int,
                       on_generation=on_generation,
                       allow_duplicate_genes=False)
ga_instance.run()
