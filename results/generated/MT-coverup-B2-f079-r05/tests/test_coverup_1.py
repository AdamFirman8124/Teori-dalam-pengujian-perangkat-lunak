# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f079 import decimal_to_binary


def test_decimal_to_binary_executes_return_line():
    """Calling decimal_to_binary executes line 3 (the return statement)."""
    # Basic conversion: 15 -> 1111
    assert decimal_to_binary(15) == "db1111db"
    # Another value: 32 -> 100000
    assert decimal_to_binary(32) == "db100000db"
    # Edge case: zero -> 0
    assert decimal_to_binary(0) == "db0db"
    # Edge case: one -> 1
    assert decimal_to_binary(1) == "db1db"
    # Large number: 255 -> 11111111
    assert decimal_to_binary(255) == "db11111111db"
