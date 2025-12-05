from s02 import solve_a
from common import read_lines


def test_solve_a():
    actual = solve_a(read_lines("input/02_test.txt"))

    assert actual == 1227775554
