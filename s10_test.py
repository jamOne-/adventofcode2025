from s10 import solve_a, solve_b
from common import read_lines


def test_solve_a():
    actual = solve_a(read_lines("input/10_test.txt"))

    assert actual == 7


def test_solve_b():
    actual = solve_b(read_lines("input/10_test.txt"))

    assert actual == 33


def test_solve_b_222():
    actual = solve_b(["[...] (0,1) (1,2) (0,2) {2,2,2}"])

    assert actual == 3
