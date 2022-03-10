from __future__ import annotations
from dataclasses import dataclass

import random


@dataclass
class Node:
    i: int
    next: Node = None

    def __repr__(self):
        demons = []
        node = self
        while node is not None:
            demons.append(node.i)
            node = node.next

        return " ".join(map(str, demons))


def create_random_ordering(number_of_demons: int) -> Node:
    demons = list(range(number_of_demons))
    random.shuffle(demons)
    dummy = node = Node(-1)
    for i in demons:
        node.next = Node(i)
        node = node.next

    return dummy.next
