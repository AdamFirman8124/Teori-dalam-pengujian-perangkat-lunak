# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f079 import decimal_to_binary


def test_decimal_to_binary_executes_return_line():
    """Exercise line 3 (the return statement) and verify the output format."""
    # Basic positive integers
    assert decimal_to_binary(8) == "db1000db"
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(255) == "db11111111db"

    # Edge cases: zero and one
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(1) == "db1db"

    # Verify the 'db' wrapper is always present around the binary digits
    result = decimal_to_binary(32)
    assert result.startswith("db")
    assert result.endswith("db")
    assert result[2:-2] == bin(32)[2:] == "100000"

    # Verify the binary digits match Python's bin() representation
    for value in (2, 5, 10, 100, 1023):
        assert decimal_to_binary(value) == "db" + bin(value)[2:] + "db"
