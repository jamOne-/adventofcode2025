from functools import reduce
import operator
from typing import Generator
from common import read_lines


def main():
    print(solve_a(read_lines("input/02.txt")))


def solve_a(lines: list[str]) -> int:
    ranges = parse_ranges(lines[0])
    invalid_sum = 0

    for start, end in ranges:
        invalid_sum += reduce(operator.add, invalid_ids_in_range(start, end), 0)

    return invalid_sum


def invalid_ids_in_range(start: int, end: int) -> Generator[int, None, None]:
    start_s = str(start)
    if len(start_s) % 2 == 0:
        first_invalid_half = start_s[: len(start_s) // 2]
    else:
        first_invalid_half = "1" + "0" * (len(start_s) // 2)

    current = int(first_invalid_half * 2)
    current_half = first_invalid_half
    if start <= current <= end:
        yield current

    while True:
        current_half = str(int(current_half) + 1)
        current = int(current_half * 2)

        if current <= end:
            yield current
        else:
            break


def parse_ranges(line: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for range_s in line.split(","):
        start, end = map(int, range_s.split("-"))
        ranges.append((start, end))
    return ranges


if __name__ == "__main__":
    main()
