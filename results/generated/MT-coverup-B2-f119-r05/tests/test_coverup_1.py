# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

import pytest

from f119 import match_parens


@pytest.mark.parametrize(
    ("parts", "expected"),
    [
        (["()", ""], "Yes"),
        ([")))", "((("], "Yes"),
        ([")", ")"], "No"),
        (["(", ""], "No"),
    ],
)
def test_match_parens_covers_all_check_paths(parts, expected):
    assert match_parens(parts) == expected
