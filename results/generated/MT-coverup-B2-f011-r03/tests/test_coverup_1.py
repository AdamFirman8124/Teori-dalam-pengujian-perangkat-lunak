# file: project/f011/__init__.py:4-12
# asked: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}
# gained: {"lines": [6, 7, 8, 10, 12], "branches": [[7, 8], [7, 10]]}

from f011 import string_xor


def test_string_xor_executes_equal_and_unequal_branches():
    assert string_xor("0101", "0011") == "0110"
