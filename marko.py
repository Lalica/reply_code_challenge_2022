from parser import parse, output
from collections import defaultdict
import random

f1 = 2
f2 = 2
f3 = 5
def heuristic(demon):
    return f1*demon.recover_stamina/(demon.recover_turns+1) + f2*sum(demon.fragments)/(1+len(demon.fragments)) - f3*demon.consume_stamina
path = "./05-androids-armageddon.txt"

stamina, max_stamina, turns, demons = parse("05-androids-armageddon.txt")

detup = []
for i in range(len(demons)):
    detup.append((demons[i], i))
scores = [(heuristic(demon[0]), demon) for demon in detup]
scores.sort()


seen = set()
killed = []
gain_stamina = defaultdict(int)
for turn in range(turns):
    stamina += gain_stamina[turn]

    i = scores[-turn][1][1]

    demon = demons[i]
    if i not in seen and demon.consume_stamina <= stamina:
        seen.add(i)
        killed.append(i)
        stamina -= demon.consume_stamina
        gain_stamina[turn + demon.recover_turns] += demon.recover_stamina
    else:
        turn -= 1
import scoring
print(scoring.score(killed, parse(path)))