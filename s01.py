from dataclasses import dataclass
from enum import Enum
from common import read_lines


class Direction(Enum):
    LEFT = "L"
    RIGHT = "R"


@dataclass(frozen=True)
class Instruction:
    direction: Direction
    distance: int


def main():
    print(solve_a(read_lines("input/01.txt")))
    print(solve_b(read_lines("input/01.txt")))


def solve_a(lines: list[str]) -> int:
    count = 0
    instructions = map(parse_line, lines)
    dial = 50

    for instruction in instructions:
        dial = rotate(instruction, dial)
        if dial == 0:
            count += 1

    return count


def solve_b(lines: list[str]) -> int:
    count = 0
    instructions = map(parse_line, lines)
    dial = 50

    for instruction in instructions:
        m = 1 if instruction.direction == Direction.RIGHT else -1
        added = dial + m * instruction.distance
        if dial > 0 and added <= 0:
            count += 1
        count += abs(added) // 100
        dial = added % 100

    return count


def rotate(instruction: Instruction, dial: int) -> int:
    m = 1 if instruction.direction == Direction.RIGHT else -1
    return (dial + m * instruction.distance) % 100


def parse_line(line: str) -> Instruction:
    direction = Direction.LEFT if line[0] == "L" else Direction.RIGHT
    distance = int(line[1:])
    return Instruction(direction, distance)


if __name__ == "__main__":
    main()
