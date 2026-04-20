import pytest

from your_functions import factorial


def test_factorial_of_0() -> None:
    assert factorial(0) == 1


def test_factorial_of_5() -> None:
    assert factorial(5) == 120


def test_factorial_negative_raises() -> None:
    with pytest.raises(ValueError):
        factorial(-1)
