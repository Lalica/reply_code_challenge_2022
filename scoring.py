from collections import namedtuple


Demon = namedtuple("demon", "consume_stamina recover_turns recover_stamina fragments")


def score(solution, problem):
    print(solution)
    print(problem)

    stamina, max_stamina, turns, demons = problem

    processing_demons = []
    new_demon = 0
    points = 0
    for t in range(turns):
        print(f"turn {t}")
        for i in range(len(processing_demons)):
            i_d, dt = processing_demons[i]
            demon = demons[i_d]

            if demon.recover_turns == dt:
                stamina += demon.recover_stamina
                stamina = min(stamina, max_stamina)

        print(f"stamina {stamina}")

        if new_demon < len(solution):
            demon = demons[solution[new_demon]]
            if demon.consume_stamina <= stamina:
                stamina -= demon.consume_stamina
                processing_demons.append([new_demon, 0])
                new_demon += 1

        for i in range(len(processing_demons)):
            i_d, dt = processing_demons[i]
            demon = demons[i_d]

            if dt >= len(demon.fragments):
                continue

            points += demon.fragments[dt]
            print(f"new points {demon.fragments[dt]}")
            processing_demons[i][1] += 1

        print(f"points {points}")

    return points
