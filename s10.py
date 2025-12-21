from dataclasses import dataclass
import functools
from itertools import chain, combinations
from typing import Iterable, TypeVar
from collections import defaultdict
from common import read_lines


def main():
    print(solve_a(read_lines("input/10.txt")))
    print(solve_b(read_lines("input/10.txt")))


def solve_a(lines: list[str]) -> int:
    machines = _parse_input(lines)
    return sum(map(_solve_machine_a, machines))


def solve_b(lines: list[str]) -> int:
    machines = _parse_input(lines)
    return sum(map(_solve_machine_b, machines))


@dataclass(frozen=True)
class _Button:
    lights: tuple[int, ...]
    pattern: int


@dataclass(frozen=True)
class _Machine:
    goal: int
    buttons: list[_Button]
    joltage: tuple[int, ...]


def _get_patterns_dict(buttons: list[_Button]) -> dict[int, list[set[_Button]]]:
    patterns: dict[int, list[set[_Button]]] = defaultdict(list)
    for bs in _powerset(buttons):
        pattern = 0
        for b in bs:
            pattern ^= b.pattern
        patterns[pattern].append(set(bs))
    return patterns


def _solve_machine_a(machine: _Machine) -> int:
    patterns_dict = _get_patterns_dict(machine.buttons)
    return min(map(len, patterns_dict[machine.goal]))


def _solve_machine_b(machine: _Machine) -> int:
    patterns_dict = _get_patterns_dict(machine.buttons)

    @functools.cache
    def _aux(joltage: tuple[int, ...]) -> int | None:
        if all(j == 0 for j in joltage):
            return 0
        if any(j < 0 for j in joltage):
            return None

        parity_goal = 0
        for j in joltage:
            parity_goal <<= 1
            parity_goal += j & 1

        candidates: list[int] = []

        for parity_solution in patterns_dict.get(parity_goal, []):
            smaller_joltage = list(joltage)
            for b in parity_solution:
                for l in b.lights:
                    smaller_joltage[l] -= 1
            smaller_joltage = tuple(j >> 1 for j in smaller_joltage)
            smaller_cost = _aux(smaller_joltage)
            if smaller_cost is not None:
                candidates.append(smaller_cost * 2 + len(parity_solution))

        return min(candidates, default=None)

    result = _aux(machine.joltage)
    assert result is not None
    return result


def _parse_input(lines: list[str]) -> list[_Machine]:
    machines: list[_Machine] = []
    for line in lines:
        split = line.split(" ")
        goal = _encode_goal(split[0])
        joltage_s = split[-1][1:-1]
        joltage = tuple(map(int, joltage_s.split(",")))
        buttons: list[_Button] = []
        for lights_s in split[1:-1]:
            lights_s = lights_s[1:-1]
            lights: tuple[int, ...] = tuple(map(int, lights_s.split(",")))
            button = _Button(
                lights=lights, pattern=_encode_lights(lights, n=len(joltage))
            )
            buttons.append(button)
        machines.append(_Machine(goal, buttons, joltage))

    return machines


def _encode_goal(goal: str) -> int:
    result = 0
    for c in goal[1:-1]:
        result <<= 1
        if c == "#":
            result += 1
    return result


def _encode_lights(lights: tuple[int, ...], n: int) -> int:
    result = 0
    for i in lights:
        result |= 1 << (n - i - 1)
    return result


_T = TypeVar("_T")


def _powerset(iterable: Iterable[_T]) -> Iterable[tuple[_T, ...]]:
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


if __name__ == "__main__":
    main()
