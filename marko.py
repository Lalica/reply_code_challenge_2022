from parser import parse, output
from collections import defaultdict
import random

def pick_index(demons, tleft):
    scores = list()
    for demon in demons:
        scores.append(demon.recover_stamina/(demon.recover_turns+1) + sum(demon.fragments[:tleft])/(1+len(demon.fragments[:tleft]))-demon.consume_stamina)
    return scores.index(max(scores))

stamina, max_stamina, turns, demons = parse("01-the-cloud-abyss.txt")

seen = set()
killed = []
gain_stamina = defaultdict(int)
for turn in range(turns):
    stamina += gain_stamina[turn]
    i = pick_index(demons, turns-turn)
    demon = demons[i]
    if i not in seen and demon.consume_stamina <= stamina:
        seen.add(i)
        killed.append(i)
        stamina -= demon.consume_stamina
        gain_stamina[turn + demon.recover_turns] += demon.recover_stamina
    demons.remove(demon)

print(killed)
