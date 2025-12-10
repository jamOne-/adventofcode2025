import functools
from common import parse_grid, read_lines, Point


def main():
    print(solve_a(read_lines("input/07.txt")))
    print(solve_b(read_lines("input/07.txt")))


def solve_a(lines: list[str]) -> int:
    start, grid = _parse_input(lines)

    @functools.cache
    def _count_splits(p: Point) -> frozenset[Point]:
        x, y = p
        if (x, y + 1) not in grid:
            return frozenset()
        elif grid[(x, y + 1)] == "^":
            return (
                frozenset([(x, y + 1)])
                | _count_splits((x - 1, y + 1))
                | _count_splits((x + 1, y + 1))
            )
        else:
            return _count_splits((x, y + 1))

    return len(_count_splits(start))


def solve_b(lines: list[str]) -> int:
    start, grid = _parse_input(lines)

    @functools.cache
    def _count_timelines(p: Point) -> int:
        x, y = p
        if (x, y + 1) not in grid:
            return 1
        elif grid[(x, y + 1)] == "^":
            return _count_timelines((x - 1, y + 1)) + _count_timelines((x + 1, y + 1))
        else:
            return _count_timelines((x, y + 1))

    return _count_timelines(start)


def _parse_input(
    lines: list[str],
) -> tuple[Point, dict[Point, str]]:
    parsed = parse_grid(lines)
    starts = [p for p, c in parsed.grid.items() if c == "S"]
    assert len(starts) == 1
    return starts[0], parsed.grid


if __name__ == "__main__":
    main()
