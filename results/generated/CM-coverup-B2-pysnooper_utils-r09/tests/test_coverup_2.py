# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

from pysnooper.utils import get_shortish_repr, normalize_repr, truncate


def test_get_shortish_repr_basic():
    assert get_shortish_repr(123) == "123"
    assert get_shortish_repr("hi") == "'hi'"
    assert get_shortish_repr(None) == "None"


def test_get_shortish_repr_custom_repr():
    assert get_shortish_repr(123, custom_repr=[(int, lambda x: "INT!")]) == "INT!"
    assert get_shortish_repr("hi", custom_repr=[(str, lambda x: "STR!")]) == "STR!"
    # callable condition
    assert get_shortish_repr(5, custom_repr=[(lambda x: True, lambda x: "ANY")]) == "ANY"
    # non-matching condition falls back to repr
    assert get_shortish_repr(5, custom_repr=[(str, lambda x: "STR!")]) == "5"


def test_get_shortish_repr_repr_failed():
    class BadRepr:
        def __repr__(self):
            raise RuntimeError("boom")

    assert get_shortish_repr(BadRepr()) == "REPR FAILED"

    def boom(item):
        raise ValueError("boom")

    assert get_shortish_repr(1, custom_repr=[(lambda x: True, boom)]) == "REPR FAILED"
    assert get_shortish_repr(1, custom_repr=[(int, boom)]) == "REPR FAILED"


def test_get_shortish_repr_strips_newlines():
    def with_newlines(item):
        return "a\nb\rc\nd\re"

    assert get_shortish_repr(1, custom_repr=[(lambda x: True, with_newlines)]) == "abcde"

    def with_crlf(item):
        return "hello\r\nworld"

    assert get_shortish_repr(1, custom_repr=[(lambda x: True, with_crlf)]) == "helloworld"


def test_get_shortish_repr_normalize_false_preserves_address():
    obj = object()
    raw = repr(obj).replace("\r", "").replace("\n", "")
    assert "0x" in raw
    result = get_shortish_repr(obj)
    assert result == raw
    assert "0x" in result


def test_get_shortish_repr_normalize_true():
    obj = object()
    result = get_shortish_repr(obj, normalize=True)
    expected = normalize_repr(repr(obj).replace("\r", "").replace("\n", ""))
    assert result == expected
    assert "0x" not in result

    def addr_repr(item):
        return "<MyClass object at 0x12345678>"

    result2 = get_shortish_repr(1, custom_repr=[(lambda x: True, addr_repr)], normalize=True)
    assert result2 == normalize_repr("<MyClass object at 0x12345678>")
    assert "0x" not in result2


def test_get_shortish_repr_max_length():
    # falsy max_length: no truncation
    assert get_shortish_repr("hi", max_length=None) == "'hi'"
    assert get_shortish_repr("hi", max_length=100) == "'hi'"
    assert get_shortish_repr(123, max_length=0) == "123"
    # truthy max_length that does not truncate because short enough
    assert get_shortish_repr("hi", max_length=10) == truncate("'hi'", 10)
    # truthy max_length that truncates
    result = get_shortish_repr("1234567890", max_length=7)
    assert result == truncate("'1234567890'", 7)
    assert result == "'1...0'"
    assert len(result) == 7
    assert "..." in result


def test_get_shortish_repr_combined_normalize_and_truncate_and_newlines():
    def messy(item):
        return "ab\ncd\r<Obj object at 0xABCDEF1234567890>efghijklmnop"

    raw_stripped = "abcd<Obj object at 0xABCDEF1234567890>efghijklmnop"
    normalized = normalize_repr(raw_stripped)
    assert "0x" not in normalized
    result = get_shortish_repr(
        1,
        custom_repr=[(lambda x: True, messy)],
        normalize=True,
        max_length=10,
    )
    assert result == truncate(normalized, 10)
    assert len(result) == 10
    assert "\n" not in result
    assert "\r" not in result
