import pytest
import pathlib
from main import get_result, get_result2


def test_1():
    data = [line for line in pathlib.Path("input_test.txt").read_text().split("\n")]
    assert get_result(data) == 5

def test_2():
    data = [line for line in pathlib.Path("input_test.txt").read_text().split("\n")]
    assert get_result2(data) == 8
