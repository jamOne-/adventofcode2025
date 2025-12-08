from s04 import solve_a, solve_b
from common import read_lines


def test_solve_a():
    actual = solve_a(read_lines("input/04_test.txt"))

    assert actual == 13


def test_solve_b():
    actual = solve_b(read_lines("input/04_test.txt"))

    assert actual == 0
