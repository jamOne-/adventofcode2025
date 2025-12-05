from s01 import solve_a, solve_b
from common import read_lines


def test_solve_a():
    actual = solve_a(read_lines("input/01_test.txt"))

    assert actual == 3


def test_solve_b():
    actual = solve_b(read_lines("input/01_test.txt"))

    assert actual == 6
