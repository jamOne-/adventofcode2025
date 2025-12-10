from s06 import solve_a, solve_b
from common import read_lines


def test_solve_a():
    actual = solve_a(read_lines("input/06_test.txt"))

    assert actual == 4277556


def test_solve_b():
    actual = solve_b(read_lines("input/06_test.txt", strip=False))

    assert actual == 3263827
