"""Simple math operations.

Kept deliberately small so each function is easy to reason about and
easy to write unit tests for.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
