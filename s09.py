from common import Point, read_lines


def main():
    print(solve_a(read_lines("input/09.txt")))
    print(solve_b(read_lines("input/09.txt")))


def solve_a(lines: list[str]) -> int:
    red_tiles = _parse_input(lines)

    largest_area = 0
    for i, p in enumerate(red_tiles):
        for p2 in red_tiles[i + 1 :]:
            area = (abs(p[0] - p2[0]) + 1) * (abs(p[1] - p2[1]) + 1)
            largest_area = max(largest_area, area)

    return largest_area


def solve_b(lines: list[str]) -> int:
    return 0


def _parse_input(lines: list[str]) -> list[Point]:
    return [tuple(map(int, line.split(","))) for line in lines]


if __name__ == "__main__":
    main()
