from collections import namedtuple


Demon = namedtuple("demon", "consume_stamina recover_turns recover_stamina fragments")


def parse(path: str) -> tuple[int, int, int, Demon]:
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
