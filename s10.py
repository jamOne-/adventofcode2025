from dataclasses import dataclass
from common import read_lines
from collections import deque


def main():
    print(solve_a(read_lines("input/10.txt")))
    print(solve_b(read_lines("input/10.txt")))


def solve_a(lines: list[str]) -> int:
    machines = _parse_input(lines)
    return sum(map(_solve_machine, machines))


def solve_b(lines: list[str]) -> int:
    return 0


@dataclass
class _Machine:
    goal: int
    buttons: list[int]
    joltage: list[int]


def _solve_machine(machine: _Machine) -> int:
    q: deque[tuple[int, int]] = deque([(0, 0)])
    visited: set[int] = set([0])

    while q:
        state, steps = q.popleft()

        if state == machine.goal:
            return steps

        for button in machine.buttons:
            new_state = state ^ button
            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, steps + 1))

    return -1


def _parse_input(lines: list[str]) -> list[_Machine]:
    machines: list[_Machine] = []
    for line in lines:
        split = line.split(" ")
        goal = _encode_goal(split[0])
        joltage_s = split[-1][1:-1]
        joltage = list(map(int, joltage_s.split(",")))
        buttons: list[int] = []
        for lights_s in split[1:-1]:
            lights_s = lights_s[1:-1]
            lights: list[int] = list(map(int, lights_s.split(",")))
            button = _encode_lights(lights)
            buttons.append(button)
        machines.append(_Machine(goal, buttons, joltage))

    return machines


def _encode_goal(goal: str) -> int:
    result = 0
    for c in reversed(goal[1:-1]):
        result <<= 1
        if c == "#":
            result += 1
    return result


def _encode_lights(lights: list[int]) -> int:
    result = 0
    for i in lights:
        result |= 1 << i
    return result


if __name__ == "__main__":
    main()
