# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pytest

from pysnooper.utils import normalize_repr


@pytest.mark.parametrize(
    ("item_repr", "expected"),
    [
        ("<object object at 0xABCDEF>", "<object object>"),
        ("value at 0x1234", "value"),
        ("prefix at 0x1A2B suffix at 0xDEADBEEF", "prefix suffix"),
        ("<object object at 0xabc>", "<object object at 0xabc>"),
        ("<object object at 0xGHIJKL>", "<object object at 0xGHIJKL>"),
        ("plain representation", "plain representation"),
        ("", ""),
    ],
)
def test_normalize_repr_removes_matching_memory_addresses(item_repr, expected):
    assert normalize_repr(item_repr) == expected
