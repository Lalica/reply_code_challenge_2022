from parser import parse, output
from scoring import score
import random

start_stamina, max_stamina, turns, demons = parse("./00-example.txt")
output([1, 3, 2, 4, 0])

problem = parse("./00-example.txt")

# solution = list(range(len(problem[3])))
# # random.shuffle(solution)
# solution = [1, 3, 2, 4, 0]
# print(score(solution, problem))
