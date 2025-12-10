from dataclasses import dataclass
from common import read_lines
import math


def main():
    print(solve_a(read_lines("input/06.txt")))
    print(solve_b(read_lines("input/06.txt", strip=False)))


def solve_a(lines: list[str]) -> int:
    parsed = _parse_input(lines)
    grid, operations = parsed.grid, parsed.operations

    results: list[int] = grid[0]
    for line in grid[1:]:
        for j, op in enumerate(operations):
            if op == "+":
                results[j] += line[j]
            elif op == "*":
                results[j] *= line[j]

    return sum(results)


def solve_b(lines: list[str]) -> int:
    result = 0
    current_nums: list[int] = []

    for c in range(len(lines[0]) - 1, -1, -1):
        column = _get_column(lines, c)

        if not column.strip():
            continue

        current_nums.append(int(column[:-1].strip()))

        if column[-1] == "+" or column[-1] == "*":
            if column[-1] == "+":
                result += sum(current_nums)
            else:
                result += math.prod(current_nums)
            current_nums = []

    return result


def _get_column(lines: list[str], c: int) -> str:
    return "".join(line[c] for line in lines)


@dataclass(frozen=True)
class _Input06:
    grid: list[list[int]]
    operations: list[str]


def _parse_input(lines: list[str]) -> _Input06:
    grid: list[list[int]] = []

    for line in lines[:-1]:
        grid.append(list(map(int, line.split())))

    operations = lines[-1].split()
    assert len(grid[0]) == len(operations)

    return _Input06(grid, operations)


if __name__ == "__main__":
    main()
