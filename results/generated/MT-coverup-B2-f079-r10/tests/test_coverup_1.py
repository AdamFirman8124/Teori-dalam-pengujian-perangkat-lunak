# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f079 import decimal_to_binary


def test_decimal_to_binary_basic():
    """Execute line 3 with typical positive integers and verify the db-wrapped binary output."""
    assert decimal_to_binary(15) == "db1111db"
    assert decimal_to_binary(32) == "db100000db"


def test_decimal_to_binary_edge_cases():
    """Cover edge cases: zero, one, and a larger number."""
    assert decimal_to_binary(0) == "db0db"
    assert decimal_to_binary(1) == "db1db"
    assert decimal_to_binary(255) == "db11111111db"
