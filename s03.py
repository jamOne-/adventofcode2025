from common import read_lines


def main():
    print(solve_a(read_lines("input/03.txt")))
    print(solve_b(read_lines("input/03.txt")))


def solve_a(lines: list[str]) -> int:
    parsed = parse_lines(lines)
    sum = 0

    for line in parsed:
        highest = max(line)
        highest_i = line.index(highest)

        if highest_i == len(line) - 1:
            first_digit = max(line[:highest_i])
            second_digit = highest
        else:
            first_digit = highest
            second_digit = max(line[highest_i + 1 :])

        sum += first_digit * 10 + second_digit

    return sum


def solve_b(lines: list[str]) -> int:
    return 0


def parse_lines(lines: list[str]) -> list[list[int]]:
    return [list(map(int, line)) for line in lines]


if __name__ == "__main__":
    main()
