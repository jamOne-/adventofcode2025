from functools import reduce
import operator
from typing import Generator
from common import read_lines


def main():
    print(solve_a(read_lines("input/02.txt")))
    print(solve_b(read_lines("input/02.txt")))


def solve_a(lines: list[str]) -> int:
    ranges = parse_ranges(lines[0])
    invalid_sum = 0

    for start, end in ranges:
        invalid_sum += reduce(operator.add, invalid_ids_in_range(start, end, n=2), 0)

    return invalid_sum


def solve_b(lines: list[str]) -> int:
    ranges = parse_ranges(lines[0])
    invalid_sum = 0

    for start, end in ranges:
        invalid_ids: set[int] = set()
        for n in range(2, len(str(end)) + 1):
            invalid_ids.update(invalid_ids_in_range(start, end, n=n))
        invalid_sum += reduce(operator.add, invalid_ids, 0)

    return invalid_sum


def invalid_ids_in_range(start: int, end: int, n: int) -> Generator[int, None, None]:
    start_s = str(start)
    if len(start_s) % n == 0:
        current_part = start_s[: len(start_s) // n]
    else:
        current_part = "1" + "0" * (len(start_s) // n)

    current = int(current_part * n)

    while current <= end:
        if start <= current <= end:
            yield current

        current_part = str(int(current_part) + 1)
        current = int(current_part * n)


def parse_ranges(line: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for range_s in line.split(","):
        start, end = map(int, range_s.split("-"))
        ranges.append((start, end))
    return ranges


if __name__ == "__main__":
    main()
