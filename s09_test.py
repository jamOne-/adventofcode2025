from s09 import solve_a, solve_b
from common import read_lines


def test_solve_a():
    actual = solve_a(read_lines("input/09_test.txt"))

    assert actual == 50


def test_solve_b():
    actual = solve_b(read_lines("input/09_test.txt"))

    assert actual == 24
