from parser import parse, output
from scoring import score


def test(problem_filename, solution_filename):
    problem = parse(problem_filename)

    with open(solution_filename) as f:
        solution = list(map(int, f.read().strip().split()))

    print(score(solution, problem))
