# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f097 import multiply


def test_multiply_uses_absolute_last_digits():
    assert multiply(123, 456) == 18


def test_multiply_handles_negative_numbers():
    assert multiply(-123, -456) == 28
    assert multiply(-123, 456) == 42
