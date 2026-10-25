# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

from pysnooper.utils import DEFAULT_REPR_RE, get_shortish_repr, normalize_repr


def test_normalize_repr_removes_memory_address():
    assert normalize_repr("<object object at 0x7f8b8c0d5e00>") == "<object object>"
    assert normalize_repr("<WithAddress at 0x1234ABCD>") == "<WithAddress>"
    assert normalize_repr("<A at 0xABCDEF> and <B at 0x123456>") == "<A> and <B>"
    result = normalize_repr(repr(object()))
    assert result == "<object object>"
    assert "at 0x" not in result
    assert result == DEFAULT_REPR_RE.sub("", repr(object()))


def test_normalize_repr_leaves_plain_repr_unchanged():
    assert normalize_repr("<object object>") == "<object object>"
    assert normalize_repr("hello") == "hello"
    assert normalize_repr("") == ""
    # Regex requires at least 4 hex digits, so short addresses are kept
    assert normalize_repr("foo at 0x12") == "foo at 0x12"
    assert normalize_repr("foo at 0x12AB") == "foo"


def test_get_shortish_repr_normalize_true_covers_normalize_repr():
    class WithAddress:
        def __repr__(self):
            return "<WithAddress at 0x1234ABCD>"

    item = WithAddress()
    normalized = get_shortish_repr(item, normalize=True)
    assert normalized == "<WithAddress>"
    assert "at 0x" not in normalized

    unnormalized = get_shortish_repr(item, normalize=False)
    assert unnormalized == "<WithAddress at 0x1234ABCD>"
    assert "at 0x" in unnormalized

    # default (normalize=False) preserves address, explicit True strips it
    assert get_shortish_repr(item) == unnormalized
    assert get_shortish_repr(item, normalize=True) == normalize_repr(repr(item))
