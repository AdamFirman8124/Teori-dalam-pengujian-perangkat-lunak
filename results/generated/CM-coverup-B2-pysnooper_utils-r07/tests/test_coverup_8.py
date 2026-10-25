# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pytest

from pysnooper.utils import normalize_repr


@pytest.mark.parametrize(
    ("item_repr", "expected"),
    [
        ("<object object at 0x1A2b3C4D>", "<object object>"),
        ("<CustomObject at 0xabcdef1234>", "<CustomObject>"),
        ("plain representation", "plain representation"),
    ],
)
def test_normalize_repr_removes_memory_address_or_preserves_repr(
    item_repr, expected
):
    assert normalize_repr(item_repr) == expected
