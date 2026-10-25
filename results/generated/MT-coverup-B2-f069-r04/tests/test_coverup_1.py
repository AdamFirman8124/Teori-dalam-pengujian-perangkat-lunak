# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

import pytest

from f069 import search


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([4, 1, 2, 2, 3, 1], 2),
        ([1, 2, 2, 3, 3, 3, 4, 4, 4], 3),
        ([5, 5, 4, 4, 4], -1),
    ],
)
def test_search(values, expected):
    assert search(values) == expected
