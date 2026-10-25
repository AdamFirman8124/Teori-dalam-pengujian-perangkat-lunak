# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import pytest

from pysnooper.utils import normalize_repr


def test_normalize_repr_removes_memory_address():
    assert normalize_repr("<Foo object at 0x7f8b8c0d1234>") == "<Foo object>"


def test_normalize_repr_without_address_unchanged():
    assert normalize_repr("<Foo object>") == "<Foo object>"
    assert normalize_repr("plain string") == "plain string"
    assert normalize_repr("") == ""


def test_normalize_repr_removes_uppercase_hex_address():
    assert normalize_repr("<Bar object at 0xABCDEF1234>") == "<Bar object>"


def test_normalize_repr_removes_mixed_case_hex_address():
    assert normalize_repr("<Baz object at 0xAbCdEf12>") == "<Baz object>"


def test_normalize_repr_short_address_not_removed():
    # Pattern requires at least 4 hex digits after 0x
    assert normalize_repr("<Foo object at 0x123>") == "<Foo object at 0x123>"
    assert normalize_repr("<Foo object at 0x12>") == "<Foo object at 0x12>"


def test_normalize_repr_removes_all_occurrences():
    assert (
        normalize_repr("<A at 0x1234> <B at 0xabcdef>")
        == "<A> <B>"
    )


def test_normalize_repr_real_object_repr():
    obj = object()
    result = normalize_repr(repr(obj))
    assert " at 0x" not in result
    assert result == "<object object>"


@pytest.mark.parametrize(
    "item_repr,expected",
    [
        ("<Foo object at 0x1234>", "<Foo object>"),
        ("<Foo object at 0xdeadBEEF99>", "<Foo object>"),
        ("no address here", "no address here"),
        ("at 0x1234 without leading space", "at 0x1234 without leading space"),
        ("<Foo object at 0xZZZZ>", "<Foo object at 0xZZZZ>"),
    ],
)
def test_normalize_repr_parametrized(item_repr, expected):
    assert normalize_repr(item_repr) == expected
