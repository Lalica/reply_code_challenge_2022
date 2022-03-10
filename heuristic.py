from parser import parse, output
from scoring import score
from collections import defaultdict
import random

paths = [
    "./00-example.txt",
    "./01-the-cloud-abyss.txt",
    "./02-iot-island-of-terror.txt",
    "./03-etheryum.txt",
    "./04-the-desert-of-autonomous-machines.txt",
    "./05-androids-armageddon.txt",
]


def main(path: str):
    stamina, max_stamina, turns, demons = parse(path)

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

    filename = output(killed)
    print(f"{filename}: ", score(killed, parse(path)))


for path in paths:
    main(path)
