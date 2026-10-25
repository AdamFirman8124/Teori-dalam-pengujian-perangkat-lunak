# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

from pysnooper.utils import normalize_repr


def test_normalize_repr_removes_memory_address():
    item_repr = "<Example object at 0xABCDEF12>"

    result = normalize_repr(item_repr)

    assert result == "<Example object>"


def test_normalize_repr_preserves_repr_without_memory_address():
    item_repr = "<Example object>"

    result = normalize_repr(item_repr)

    assert result == item_repr
