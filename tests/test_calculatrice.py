from calc import calculate
import pytest


def test_addition():
    assert calculate("+", 2, 3) == 5
    assert calculate("+", -1, 1) == 0
    assert calculate("+", 0, 0) == 0


def test_subtraction():
    assert calculate("-", 5, 3) == 2
    assert calculate("-", 3, 5) == -2
    assert calculate("-", -1, -1) == 0


def test_multiplication():
    assert calculate("*", 4, 3) == 12
    assert calculate("*", -2, 3) == -6
    assert calculate("*", 0, 10) == 0


def test_division():
    assert calculate("/", 10, 2) == 5
    assert calculate("/", -9, 3) == -3
    assert calculate("/", 1, 2) == 0.5


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("/", 1, 0)


def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate("%", 1, 2)
    with pytest.raises(ValueError):
        calculate("x", 1, 2)
