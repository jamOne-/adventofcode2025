from common import read_lines, Point3
import math


class _Node:

    def __init__(self, p: Point3):
        self.parent: _Node | None = None
        self.size = 1
        self.p = p


def main():
    print(solve_a(read_lines("input/08.txt")))
    print(solve_b(read_lines("input/08.txt")))


def solve_a(lines: list[str], n: int = 1000) -> int:
    boxes = _parse_input(lines)
    nodes = [_Node(box) for box in boxes]
    distances = _calculate_distances(nodes)

    n_nodes = sorted(distances.items(), key=lambda kv: kv[1])[:n]
    for (node1, node2), _ in n_nodes:
        _union(node1, node2)

    parents = [node for node in nodes if node.parent is None]
    parents = sorted(parents, key=lambda n: n.size, reverse=True)

    assert len(parents) >= 3
    return parents[0].size * parents[1].size * parents[2].size


def solve_b(lines: list[str]) -> int:
    return 0


def _parse_input(lines: list[str]) -> list[Point3]:
    return [tuple(map(int, line.split(","))) for line in lines]


def _calculate_distances(nodes: list[_Node]) -> dict[tuple[_Node, _Node], float]:
    distances: dict[tuple[_Node, _Node], float] = {}
    for i in range(len(nodes) - 1):
        for j in range(i + 1, len(nodes)):
            d = math.dist(nodes[i].p, nodes[j].p)
            distances[(nodes[i], nodes[j])] = d

    return distances


def _union(a: _Node, b: _Node) -> None:
    ap = _find_parent(a)
    bp = _find_parent(b)

    if ap == bp:
        return
    if ap.size < bp.size:
        bp.parent = ap
        ap.size += bp.size
    else:
        ap.parent = bp
        bp.size += ap.size


def _find_parent(node: _Node) -> _Node:
    if node.parent is None:
        return node
    node.parent = _find_parent(node.parent)
    return node.parent


if __name__ == "__main__":
    main()
