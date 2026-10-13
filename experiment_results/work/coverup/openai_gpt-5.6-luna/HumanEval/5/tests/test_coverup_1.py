# file: script_5.py:4-22
# asked: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}
# gained: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}

from script_5 import intersperse


def test_intersperse_returns_empty_list_for_empty_input():
    numbers = []

    result = intersperse(numbers, 4)

    assert result == []
    assert numbers == []


def test_intersperse_inserts_delimeter_between_multiple_numbers():
    numbers = [1, 2, 3]

    result = intersperse(numbers, 4)

    assert result == [1, 4, 2, 4, 3]
    assert numbers == [1, 2, 3]


def test_intersperse_returns_single_number_without_delimeter():
    numbers = [7]

    result = intersperse(numbers, 0)

    assert result == [7]
    assert numbers == [7]
