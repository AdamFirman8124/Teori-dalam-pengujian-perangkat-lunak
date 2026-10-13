# file: script_5.py:4-22
# asked: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}
# gained: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}

from script_5 import intersperse


def test_intersperse_empty_list():
    numbers = []

    result = intersperse(numbers, 4)

    assert result == []
    assert numbers == []


def test_intersperse_inserts_delimiter_between_all_elements():
    numbers = [1, 2, 3]

    result = intersperse(numbers, 4)

    assert result == [1, 4, 2, 4, 3]
    assert numbers == [1, 2, 3]
