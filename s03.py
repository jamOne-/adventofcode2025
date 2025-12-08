from common import read_lines
from functools import reduce
import operator


def main():
    print(solve_a(read_lines("input/03.txt")))
    print(solve_b(read_lines("input/03.txt")))


def solve_a(lines: list[str]) -> int:
    return reduce(
        operator.add, map(lambda line: find_biggest_battery(line, n=2), lines), 0
    )


def solve_b(lines: list[str]) -> int:
    return reduce(
        operator.add, map(lambda line: find_biggest_battery(line, n=12), lines), 0
    )


def find_biggest_battery(xs: str, n: int) -> int:
    battery = ["0" for _ in range(n)]

    for i, x in enumerate(xs):
        nums_left = len(xs) - i - 1
        for j in range(max(0, n - nums_left - 1), n):
            if x > battery[j]:
                battery[j] = x
                for k in range(j + 1, n):
                    battery[k] = "0"
                break

    return int("".join(battery))


if __name__ == "__main__":
    main()
