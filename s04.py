from collections import deque
from common import get_neighbors, read_lines, parse_grid


def main():
    print(solve_a(read_lines("input/04.txt")))
    print(solve_b(read_lines("input/04.txt")))


def solve_a(lines: list[str]) -> int:
    grid = parse_grid(lines)

    count = 0
    for x in range(grid.size[0]):
        for y in range(grid.size[1]):
            if grid.grid[(x, y)] == "@":
                if len(get_adjacent_rolls(grid.grid, x, y)) < 4:
                    count += 1

    return count


def solve_b(lines: list[str]) -> int:
    grid = parse_grid(lines)
    rolls: dict[tuple[int, int], set[tuple[int, int]]] = {}

    for x in range(grid.size[0]):
        for y in range(grid.size[1]):
            if grid.grid[(x, y)] == "@":
                rolls[(x, y)] = get_adjacent_rolls(grid.grid, x, y)

    count = 0
    q: deque[tuple[int, int]] = deque([p for p, rs in rolls.items() if len(rs) < 4])
    while q:
        p = q.popleft()
        if p not in rolls:
            continue
        for r in rolls[p]:
            rolls[r].remove(p)
            if len(rolls[r]) < 4:
                q.append(r)
        del rolls[p]
        count += 1

    return count


def get_adjacent_rolls(
    grid: dict[tuple[int, int], str], x: int, y: int
) -> set[tuple[int, int]]:
    adjacent_rolls: set[tuple[int, int]] = set()
    for nx, ny in get_neighbors(x, y):
        if grid.get((nx, ny), None) == "@":
            adjacent_rolls.add((nx, ny))

    return adjacent_rolls


if __name__ == "__main__":
    main()
