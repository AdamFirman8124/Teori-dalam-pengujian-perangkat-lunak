# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

import pytest

from script_0 import has_close_elements


@pytest.mark.parametrize(
    ("numbers", "threshold", "expected"),
    [
        ([1.0, 2.0, 3.0], 0.5, False),
        ([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3, True),
        ([1.0, 2.0], 1.0, False),
        ([1.0, 1.0], 0.1, True),
        ([], 1.0, False),
        ([1.0], 1.0, False),
    ],
)
def test_has_close_elements(numbers, threshold, expected):
    assert has_close_elements(numbers, threshold) is expected
