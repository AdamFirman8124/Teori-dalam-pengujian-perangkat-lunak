# file: project/f044/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7]]}

import pytest

from f044 import change_base


@pytest.mark.parametrize(
    ("x", "base", "expected"),
    [
        (10, 2, "1010"),
        (15, 10, "15"),
        (0, 2, ""),
    ],
)
def test_change_base(x: int, base: int, expected: str) -> None:
    assert change_base(x, base) == expected
