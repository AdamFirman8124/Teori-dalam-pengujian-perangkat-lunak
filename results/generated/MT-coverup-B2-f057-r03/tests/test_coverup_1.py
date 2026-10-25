# file: project/f057/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f057 import monotonic


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([1, 2, 2, 3], True),
        ([3, 2, 2, 1], True),
        ([1, 3, 2], False),
    ],
)
def test_monotonic(values, expected):
    assert monotonic(values) is expected
