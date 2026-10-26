# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

from pysnooper.utils import get_shortish_repr, truncate, normalize_repr


def test_get_shortish_repr_basic():
    assert get_shortish_repr(42) == "42"
    assert get_shortish_repr(42, normalize=False, max_length=None) == repr(42)


def test_get_shortish_repr_repr_failed():
    def failing_repr(item):
        raise RuntimeError("boom")

    result = get_shortish_repr(42, custom_repr=[(int, failing_repr)])
    assert result == "REPR FAILED"


def test_get_shortish_repr_strips_newlines():
    def multi_repr(item):
        return "a\nb\rc\nd"

    result = get_shortish_repr(0, custom_repr=[(object, multi_repr)])
    assert result == "abcd"
    assert "\n" not in result
    assert "\r" not in result


def test_get_shortish_repr_normalize():
    obj = object()
    raw = repr(obj)
    assert "0x" in raw

    normalized = get_shortish_repr(obj, normalize=True)
    assert normalized == normalize_repr(raw.replace("\r", "").replace("\n", ""))
    assert "0x" not in normalized

    not_normalized = get_shortish_repr(obj, normalize=False)
    assert not_normalized == raw
    assert "0x" in not_normalized


def test_get_shortish_repr_max_length():
    def long_repr(item):
        return "x" * 100

    custom = [(lambda item: True, long_repr)]
    full = get_shortish_repr(0, custom_repr=custom, max_length=None)
    assert full == "x" * 100

    # falsy max_length means no truncation
    assert get_shortish_repr(0, custom_repr=custom, max_length=0) == "x" * 100

    truncated = get_shortish_repr(0, custom_repr=custom, max_length=10)
    assert truncated == truncate("x" * 100, 10)
    assert len(truncated) == 10
    assert truncated == "xxx...xxxx"

    # short value is unchanged even with large max_length
    assert get_shortish_repr("hi", max_length=100) == repr("hi")


def test_get_shortish_repr_custom_repr_type_condition():
    result = get_shortish_repr(5, custom_repr=[(int, lambda x: "INT!")])
    assert result == "INT!"
    # non-matching type falls through to repr
    assert get_shortish_repr(5, custom_repr=[(str, lambda x: "STR!")]) == "5"


def test_get_shortish_repr_combined_normalize_and_truncate():
    def failing_repr(item):
        raise ValueError("bad")

    result = get_shortish_repr(
        42,
        custom_repr=[(int, failing_repr)],
        normalize=True,
        max_length=5,
    )
    assert result == truncate(normalize_repr("REPR FAILED"), 5)
    assert result == "R...D"

    def long_repr_with_newlines(item):
        return "a\n" + "y" * 100 + "\r" + repr(object())

    item = object()
    raw = long_repr_with_newlines(item).replace("\r", "").replace("\n", "")
    expected = truncate(normalize_repr(raw), 20)
    result2 = get_shortish_repr(
        item,
        custom_repr=[(object, long_repr_with_newlines)],
        normalize=True,
        max_length=20,
    )
    assert result2 == expected
    assert len(result2) == 20
    assert "\n" not in result2
    assert "\r" not in result2
