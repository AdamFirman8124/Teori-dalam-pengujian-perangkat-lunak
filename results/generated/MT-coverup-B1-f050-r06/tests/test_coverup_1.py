# file: project/f050/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f050 import encode_shift


def test_encode_shift_handles_regular_and_wrapping_letters():
    assert encode_shift("abcxyz") == "fghcde"


def test_encode_shift_handles_empty_string():
    assert encode_shift("") == ""
