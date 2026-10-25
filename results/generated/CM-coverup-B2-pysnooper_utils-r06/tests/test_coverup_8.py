# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pytest

from pysnooper.utils import normalize_repr


@pytest.mark.parametrize(
    ("item_repr", "expected"),
    [
        (
            "<Example object at 0x7F12ABCD>",
            "<Example object>",
        ),
        (
            "<Example object at 0xdeadBEEF>",
            "<Example object>",
        ),
        (
            "plain representation",
            "plain representation",
        ),
        (
            "<Example object at 0xabc>",
            "<Example object at 0xabc>",
        ),
    ],
)
def test_normalize_repr(item_repr, expected):
    assert normalize_repr(item_repr) == expected
