# file: script_5.py:4-22
# asked: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}
# gained: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}

from script_5 import intersperse


def test_intersperse_empty_list():
    assert intersperse([], 4) == []


def test_intersperse_inserts_delimiter_between_elements():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
