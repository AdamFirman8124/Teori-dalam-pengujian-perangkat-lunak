# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f079 import decimal_to_binary


def test_decimal_to_binary():
    # Basic positive integers
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"

    # Edge cases: 0 and 1
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(1) == "db1db"

    # Larger value
    assert decimal_to_binary(255) == "db11111111db"
