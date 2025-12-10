from dataclasses import dataclass
from typing import Generator

Point = tuple[int, int]


@dataclass(frozen=True)
class Grid:
    grid: dict[Point, str]
    size: tuple[int, int]


def read_lines(filename: str, strip: bool = True) -> list[str]:
    with open(filename, encoding="UTF-8") as f:
        lines = f.readlines()
    return [line.strip() if strip else line for line in lines]


def parse_grid(lines: list[str]) -> Grid:
    grid: dict[Point, str] = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    size = len(lines[0]), len(lines)
    return Grid(grid, size)


def get_neighbors(x: int, y: int) -> Generator[Point, None, None]:
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            yield x + dx, y + dy
