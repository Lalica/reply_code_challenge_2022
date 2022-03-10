from collections import namedtuple
from datetime import datetime


Demon = namedtuple("demon", "consume_stamina recover_turns recover_stamina fragments")
task = None


def parse(path: str) -> tuple[int, int, int, Demon]:
    global task
    task = path.split("/")[-1][:2]
    demons = []
    with open(path) as f:
        start_stamina, max_stamina, turns, _ = next(f).strip().split()
        for line in f:
            (
                consume_stamina,
                recover_turns,
                recover_stamina,
                _,
                *fragments,
            ) = line.strip().split()
            demons.append(
                Demon(consume_stamina, recover_turns, recover_stamina, fragments)
            )

    return start_stamina, max_stamina, turns, demons


def output(arr: list) -> None:
    global task
    with open(f"sol{task}-" + datetime.now().strftime("%H-%M-%S") + ".txt", "w") as f:
        for i in arr:
            print(i, file=f)
