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
    connecting_order = _calculate_distances(nodes)

    for (node1, node2), _ in connecting_order[:n]:
        _union(node1, node2)

    parents = [node for node in nodes if node.parent is None]
    parents = sorted(parents, key=lambda n: n.size, reverse=True)

    assert len(parents) >= 3
    return parents[0].size * parents[1].size * parents[2].size


def solve_b(lines: list[str]) -> int:
    boxes = _parse_input(lines)
    nodes = [_Node(box) for box in boxes]
    connecting_order = _calculate_distances(nodes)

    for (node1, node2), _ in connecting_order:
        p = _union(node1, node2)
        if p.size == len(nodes):
            return node1.p[0] * node2.p[0]

    return 0


def _parse_input(lines: list[str]) -> list[Point3]:
    return [tuple(map(int, line.split(","))) for line in lines]


def _calculate_distances(nodes: list[_Node]) -> list[tuple[tuple[_Node, _Node], float]]:
    distances: list[tuple[tuple[_Node, _Node], float]] = []
    for i in range(len(nodes) - 1):
        for j in range(i + 1, len(nodes)):
            d = math.dist(nodes[i].p, nodes[j].p)
            distances.append(((nodes[i], nodes[j]), d))

    return sorted(distances, key=lambda nd: nd[1])


def _union(a: _Node, b: _Node) -> _Node:
    ap = _find_parent(a)
    bp = _find_parent(b)
    if ap == bp:
        return ap

    parent, child = (bp, ap) if ap.size < bp.size else (ap, bp)
    child.parent = parent
    parent.size += child.size
    return parent


def _find_parent(node: _Node) -> _Node:
    if node.parent is None:
        return node
    node.parent = _find_parent(node.parent)
    return node.parent


if __name__ == "__main__":
    main()
