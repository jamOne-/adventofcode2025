from common import parse_grid, read_lines, Point
from collections import deque


def main():
    print(solve_a(read_lines("input/07.txt")))
    print(solve_b(read_lines("input/07.txt")))


def solve_a(lines: list[str]) -> int:
    start, grid = _parse_input(lines)
    visited: set[Point] = set([start])
    q: deque[Point] = deque([start])
    split_count = 0

    while q:
        x, y = q.popleft()
        new_ps: list[Point] = []

        if (x, y + 1) not in grid:
            continue
        elif grid[(x, y + 1)] == "^":
            new_ps = [(x - 1, y + 1), (x + 1, y + 1)]
            split_count += 1
        else:
            new_ps = [(x, y + 1)]

        for new_p in new_ps:
            if new_p not in visited and new_p in grid:
                visited.add(new_p)
                q.append(new_p)

    return split_count


def solve_b(lines: list[str]) -> int:
    return 0


def _parse_input(
    lines: list[str],
) -> tuple[Point, dict[Point, str]]:
    parsed = parse_grid(lines)
    starts = [p for p, c in parsed.grid.items() if c == "S"]
    assert len(starts) == 1
    return starts[0], parsed.grid


if __name__ == "__main__":
    main()
