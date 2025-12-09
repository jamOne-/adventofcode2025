from dataclasses import dataclass
from common import read_lines


def main():
    print(solve_a(read_lines("input/05.txt")))
    print(solve_b(read_lines("input/05.txt")))


def solve_a(lines: list[str]) -> int:
    parsed = _parse_input(lines)
    ranges, ingredients = parsed.ranges, parsed.ingredients

    count = 0
    for i in ingredients:
        for start, end in ranges:
            if start <= i <= end:
                count += 1
                break

    return count


def solve_b(lines: list[str]) -> int:
    ranges = _parse_input(lines).ranges
    ranges = sorted(ranges, key=lambda r: r[0])

    count = 0
    i = 0
    for start, end in ranges:
        ns = max(start, i + 1)
        count += max(0, end - ns + 1)
        i = max(i, end)

    return count


@dataclass(frozen=True)
class _Input05:
    ranges: list[tuple[int, int]]
    ingredients: set[int]


def _parse_input(lines: list[str]) -> _Input05:
    ranges: list[tuple[int, int]] = []

    i = 0
    for i, line in enumerate(lines):
        if not line:
            break
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ingredients = set(int(line) for line in lines[i + 1 :])
    return _Input05(ranges, ingredients)


if __name__ == "__main__":
    main()
