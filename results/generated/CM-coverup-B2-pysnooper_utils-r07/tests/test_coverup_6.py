# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

import pytest

from pysnooper.utils import ensure_tuple


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ([1, 2, 3], (1, 2, 3)),  # Iterable, non-string.
        ("text", ("text",)),      # Iterable string.
        (42, (42,)),              # Non-iterable.
    ],
)
def test_ensure_tuple_covers_all_branches(value, expected):
    assert ensure_tuple(value) == expected
