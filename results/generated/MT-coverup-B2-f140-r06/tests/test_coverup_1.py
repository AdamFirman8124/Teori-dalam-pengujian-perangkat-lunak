# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

import pytest

from f140 import fix_spaces


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("abc", "abc"),
        ("a b", "a_b"),
        ("a  b", "a__b"),
        ("a   b", "a-b"),
        ("a ", "a_"),
        ("a   ", "a-"),
    ],
)
def test_fix_spaces_covers_all_spacing_branches(text, expected):
    assert fix_spaces(text) == expected
