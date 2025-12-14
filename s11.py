from common import read_lines
from collections import defaultdict
import functools


def main():
    print(solve_a(read_lines("input/11.txt")))
    print(solve_b(read_lines("input/11.txt")))


def solve_a(lines: list[str]) -> int:
    edges = _parse_input(lines)

    @functools.cache
    def _aux(node: str) -> int:
        if node == "out":
            return 1
        if not edges.get(node, set()):
            return 0
        return sum(_aux(n) for n in edges[node])

    return _aux("you")


def solve_b(lines: list[str]) -> int:
    edges = _parse_input(lines)

    @functools.cache
    def _aux(node: str, dac: bool, fft: bool) -> int:
        if node == "out" and dac and fft:
            return 1
        if not edges.get(node, set()) or node == "out":
            return 0
        if node == "dac":
            dac = True
        elif node == "fft":
            fft = True
        return sum(_aux(n, dac, fft) for n in edges[node])

    return _aux("svr", False, False)


def _parse_input(lines: list[str]) -> dict[str, set[str]]:
    edges: dict[str, set[str]] = {}
    for line in lines:
        split = line.split(" ")
        node = split[0][:-1]
        nodes = split[1:]
        edges[node] = set(nodes)
    return edges


if __name__ == "__main__":
    main()
