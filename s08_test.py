from s08 import solve_a, solve_b
from common import read_lines


def test_solve_a():
    actual = solve_a(read_lines("input/08_test.txt"), n=10)

    assert actual == 40


def test_solve_b():
    actual = solve_b(read_lines("input/08_test.txt"))

    assert actual == 0
