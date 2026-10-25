# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pysnooper.utils as utils_module


class _WithAddress:
    def __repr__(self):
        return "<WithAddress object at 0x1234ABCD>"


class _WithoutAddress:
    def __repr__(self):
        return "<WithoutAddress object>"


def test_get_shortish_repr_normalize_removes_address():
    result = utils_module.get_shortish_repr(_WithAddress(), normalize=True)
    assert result == "<WithAddress object>"
    assert "at 0x" not in result
    assert "0x1234ABCD" not in result


def test_get_shortish_repr_without_normalize_keeps_address():
    result = utils_module.get_shortish_repr(_WithAddress(), normalize=False)
    assert result == "<WithAddress object at 0x1234ABCD>"
    assert "at 0x" in result


def test_get_shortish_repr_normalize_no_address_unchanged():
    result = utils_module.get_shortish_repr(_WithoutAddress(), normalize=True)
    assert result == "<WithoutAddress object>"


def test_get_shortish_repr_normalize_with_truncate():
    result = utils_module.get_shortish_repr(
        _WithAddress(), max_length=100, normalize=True
    )
    assert result == "<WithAddress object>"
    assert "0x" not in result
