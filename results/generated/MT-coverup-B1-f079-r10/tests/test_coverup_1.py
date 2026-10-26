# file: project/f079/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f079 import decimal_to_binary


def test_decimal_to_binary():
    assert decimal_to_binary(5) == "db101db"
