import sys
import pygad
from marko import main
from parser import parse, output


best, best_sol = 0, []


def fitness_func(solution, solution_idx):
    return main(solution, problem)


def on_generation(ga):
    global best, best_sol
    ga_best_sol, ga_best, _ = ga.best_solution()

    if ga_best > best:
        best = ga_best
        best_sol = ga_best_sol

        print(best)
        output(best_sol, sol_filename)


filename = sys.argv[1]
sol_filename = "sol" + filename[:2] + "-marko-genetski.txt"
problem = parse(filename)
N = len(problem[3])
ga_instance = pygad.GA(num_generations=50000,
                       sol_per_pop=50,
                       num_genes=3,
                       gene_space={'low': 0., 'high': 1.},
                       mutation_num_genes=3,
                       random_mutation_min_val=0.,
                       random_mutation_max_val=1.,
                       num_parents_mating=2,
                       fitness_func=fitness_func,
                       gene_type=float,
                       on_generation=on_generation)
ga_instance.run()
