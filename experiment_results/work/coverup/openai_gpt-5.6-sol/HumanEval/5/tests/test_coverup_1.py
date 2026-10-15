# file: script_5.py:4-22
# asked: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}
# gained: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}

import pytest

from script_5 import intersperse


@pytest.mark.parametrize(
    ("numbers", "delimiter", "expected"),
    [
        ([], 4, []),
        ([7], 4, [7]),
        ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
    ],
)
def test_intersperse_all_paths(numbers, delimiter, expected):
    original_numbers = numbers.copy()

    result = intersperse(numbers, delimiter)

    assert result == expected
    assert numbers == original_numbers
    assert result is not numbers
