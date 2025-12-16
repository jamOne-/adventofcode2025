from dataclasses import dataclass
from common import read_lines

_PRESENTS_COUNT = 6
_PRESENT_SIZE = 9


@dataclass
class _Present:
    index: int
    shape: list[str]


@dataclass
class _Region:
    shape: tuple[int, int]
    presents: list[int]


def main():
    print(solve_a(read_lines("input/12.txt")))


def solve_a(lines: list[str]) -> int:
    _, regions = _parse_input(lines)
    return len(list(filter(_can_fit_simplified, regions)))


def _can_fit_simplified(region: _Region) -> bool:
    total_occupied = sum(n * _PRESENT_SIZE for n in region.presents)
    return total_occupied <= region.shape[0] * region.shape[1]


def _parse_input(lines: list[str]) -> tuple[list[_Present], list[_Region]]:
    presents: list[_Present] = []
    regions: list[_Region] = []

    for i in range(_PRESENTS_COUNT):
        j = i * 5
        shape = lines[j + 1 : j + 4]
        presents.append(_Present(i, shape))

    for line in lines[_PRESENTS_COUNT * 5 :]:
        split = line.split(" ")
        region_shape = tuple(map(int, split[0][:-1].split("x")))
        region_presents = list(map(int, split[1:]))
        regions.append(_Region(region_shape, region_presents))

    return presents, regions


if __name__ == "__main__":
    main()
