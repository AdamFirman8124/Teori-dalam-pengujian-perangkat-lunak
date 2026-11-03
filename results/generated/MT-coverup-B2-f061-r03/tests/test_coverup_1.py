# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f061 import correct_bracketing


@pytest.mark.parametrize(
    ("brackets", "expected"),
    [
        # Empty input: loop body never executes (line 4 loop-exit branch),
        # falls through to the final return with depth == 0 (line 11, True).
        ("", True),
        # Covers the if-branch (line 6) and the else-branch (line 8),
        # with depth never going negative (line 9 False branch).
        ("()", True),
        ("(())", True),
        ("()()", True),
        # Depth goes negative on the first char: early return False
        # (lines 9-10, the depth < 0 True branch).
        (")", False),
        (")(", False),
        # Depth stays positive until the end: final return with
        # depth != 0 (line 11, False outcome).
        ("(()", False),
        ("(()()", False),
        # Any non-'(' character takes the else-branch (line 8),
        # driving depth negative -> early return False.
        ("a", False),
    ],
)
def test_correct_bracketing(brackets: str, expected: bool):
    result = correct_bracketing(brackets)
    assert isinstance(result, bool)
    assert result is expected
