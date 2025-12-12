from collections import defaultdict
from bisect import bisect_left
from common import Point, read_lines, sign

_SparseDict = dict[int, list[tuple[int, int]]]


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
    red_tiles = _parse_input(lines)
    tiles_sparse = _get_sparse_tiles(red_tiles)

    largest_area = 0
    for i, p1 in enumerate(red_tiles):
        for p3 in red_tiles[i + 1 :]:
            p2, p4 = (p1[0], p3[1]), (p3[0], p1[1])

            if (
                _is_edge_tiled(p1, p2, tiles_sparse)
                and _is_edge_tiled(p2, p3, tiles_sparse)
                and _is_edge_tiled(p3, p4, tiles_sparse)
                and _is_edge_tiled(p4, p1, tiles_sparse)
            ):
                area = (abs(p1[0] - p3[0]) + 1) * (abs(p1[1] - p3[1]) + 1)
                largest_area = max(largest_area, area)

    return largest_area


def _parse_input(lines: list[str]) -> list[Point]:
    return [tuple(map(int, line.split(","))) for line in lines]


def _get_border(red_tiles: list[Point]) -> set[Point]:
    border: set[Point] = set()

    for i, p1 in enumerate(red_tiles):
        p2 = red_tiles[(i + 1) % len(red_tiles)]

        dx, dy = sign(p2[0] - p1[0]), sign(p2[1] - p1[1])
        p = p1
        while p != p2:
            border.add(p)
            p = (p[0] + dx, p[1] + dy)
        border.add(p2)

    return border


def _get_sparse_tiles(red_tiles: list[Point]) -> tuple[_SparseDict, _SparseDict]:
    border = _get_border(red_tiles)
    sparse_border_x: dict[int, list[int]] = defaultdict(list)
    sparse_border_y: dict[int, list[int]] = defaultdict(list)
    for x, y in border:
        sparse_border_x[x].append(y)
        sparse_border_y[y].append(x)
    for ys in sparse_border_x.values():
        ys.sort()
    for xs in sparse_border_y.values():
        xs.sort()

    tiles_sparse_x: _SparseDict = defaultdict(list)
    tiles_sparse_y: _SparseDict = defaultdict(list)
    for x, ys in sparse_border_x.items():
        if len(ys) % 2 == 1:
            # Corner-case, let's add a known green tile, in order:
            ay = ys[-2] + 1
            by = ys[-1]
            ys[-1] = ay
            ys.append(by)
        for i in range(0, len(ys), 2):
            tiles_sparse_x[x].append((ys[i], ys[i + 1]))
    for y, xs in sparse_border_y.items():
        if len(xs) % 2 == 1:
            # Corner-case, let's add a known green tile, in order:
            ax = xs[-2] + 1
            bx = xs[-1]
            xs[-1] = ax
            xs.append(bx)
        for i in range(0, len(xs), 2):
            tiles_sparse_y[y].append((xs[i], xs[i + 1]))

    _merge_ranges(tiles_sparse_x)
    _merge_ranges(tiles_sparse_y)

    return tiles_sparse_x, tiles_sparse_y


def _merge_ranges(tiles_sparse: _SparseDict) -> None:
    """Merges non-overlapping ranges like: [(1,2),(3,4)] -> [(1,4)]."""
    for i in tiles_sparse.keys():
        new_list: list[tuple[int, int]] = []

        current_range = tiles_sparse[i][0]
        for a, b in tiles_sparse[i][1:]:
            if a == current_range[1] + 1:
                current_range = (current_range[0], b)
            else:
                new_list.append(current_range)
                current_range = (a, b)

        new_list.append(current_range)
        tiles_sparse[i] = new_list


def _is_edge_tiled(
    p1: Point, p2: Point, tiles_sparse: tuple[_SparseDict, _SparseDict]
) -> bool:
    if p1[0] == p2[0]:
        sparse_dict = tiles_sparse[0]
        i = bisect_left(sparse_dict[p1[0]], p1[1], key=lambda r: r[1])
        if i >= len(sparse_dict[p1[0]]):
            return False
        r = sparse_dict[p1[0]][i]
        return r[0] <= p1[1] <= r[1] and r[0] <= p2[1] <= r[1]
    else:
        sparse_dict = tiles_sparse[1]
        i = bisect_left(sparse_dict[p1[1]], p1[0], key=lambda r: r[1])
        if i >= len(sparse_dict[p1[1]]):
            return False
        r = sparse_dict[p1[1]][i]
        return r[0] <= p1[0] <= r[1] and r[0] <= p2[0] <= r[1]


if __name__ == "__main__":
    main()
