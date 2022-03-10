from parser import parse, output
from collections import defaultdict
import random

stamina, max_stamina, turns, demons = parse("./01-the-cloud-abyss.txt")

seen = set()
killed = []
gain_stamina = defaultdict(int)
for turn in range(turns):
    stamina += gain_stamina[turn]
    i = random.randint(0, len(demons) - 1)
    demon = demons[i]
    if i not in seen and demon.consume_stamina <= stamina:
        seen.add(i)
        killed.append(i)
        stamina -= demon.consume_stamina
        gain_stamina[turn + demon.recover_turns] += demon.recover_stamina

output(killed)
