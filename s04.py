from common import read_lines, parse_grid


def main():
    print(solve_a(read_lines("input/04.txt")))
    print(solve_b(read_lines("input/04.txt")))


def solve_a(lines: list[str]) -> int:
    grid = parse_grid(lines)

    count = 0
    for x in range(grid.size[0]):
        for y in range(grid.size[1]):
            if grid.grid[(x, y)] == "@":
                if count_adjacent_rolls(grid.grid, x, y) < 4:
                    count += 1

    return count


def solve_b(lines: list[str]) -> int:
    return 0


def count_adjacent_rolls(grid: dict[tuple[int, int], str], x: int, y: int) -> int:
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if grid.get((nx, ny), "") == "@":
                count += 1

    return count


if __name__ == "__main__":
    main()
