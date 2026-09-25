"""Unit tests for mathutils.operations.

Each test below checks one small behavior of one function. Run them with:

    pytest
"""

import pytest

from mathutils.operations import add, subtract, multiply, divide, is_prime


def test_add():
    # Basic case: two positive numbers should sum correctly.
    assert add(2, 3) == 6
    # Edge case: positive + negative should cancel out to zero.
    assert add(-1, 1) == 0


def test_subtract():
    # Basic case: subtracting a smaller number from a larger one.
    assert subtract(5, 3) == 2
    # Edge case: subtracting from zero should give a negative result.
    assert subtract(0, 5) == -5


def test_multiply():
    # Basic case: two positive numbers.
    assert multiply(4, 3) == 12
    # Edge case: a negative number times a positive one should be negative.
    assert multiply(-2, 3) == -6


def test_divide():
    # Basic case: division that comes out even.
    assert divide(10, 2) == 5
    # Case with a non-whole result, to check float division works.
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    # divide() should refuse to divide by zero and raise ValueError
    # instead of crashing with Python's default ZeroDivisionError.
    with pytest.raises(ValueError):
        divide(1, 0)


# @pytest.mark.parametrize lets us run the same test body against many
# inputs without copy-pasting it. Each (n, expected) pair below becomes
# its own test case, e.g. "test_is_prime[17-True]".
@pytest.mark.parametrize(
    "n, expected",
    [
        (1, False),   # 1 is not considered prime by definition
        (2, True),    # 2 is the smallest prime number
        (3, True),    # 3 is prime
        (4, False),   # 4 = 2 x 2, so it's not prime
        (17, True),   # 17 is a larger prime, checks the loop works past small numbers
        (18, False),  # 18 = 2 x 9, not prime
    ],
)
def test_is_prime(n, expected):
    assert is_prime(n) == expected
