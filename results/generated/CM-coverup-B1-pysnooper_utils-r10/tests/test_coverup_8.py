# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

from pysnooper.utils import DEFAULT_REPR_RE, get_shortish_repr


class _WithAddress:
    def __repr__(self):
        return "<WithAddress at 0x1234ABCD>"


def test_get_shortish_repr_normalize_removes_memory_address():
    result = get_shortish_repr(_WithAddress(), normalize=True)
    assert result == "<WithAddress>"
    assert "at 0x" not in result
    assert "0x1234ABCD" not in result
    # postcondition matches the regex directly
    assert result == DEFAULT_REPR_RE.sub("", "<WithAddress at 0x1234ABCD>")


def test_get_shortish_repr_normalize_preserves_plain_repr():
    assert get_shortish_repr(42, normalize=True) == "42"
    assert get_shortish_repr("hi", normalize=True) == "'hi'"
    assert get_shortish_repr(_WithAddress(), normalize=False) == "<WithAddress at 0x1234ABCD>"


def test_get_shortish_repr_normalize_edge_cases():
    class ShortAddr:
        def __repr__(self):
            return "foo at 0x12"

    # fewer than 4 hex digits: regex requires {4,}, so unchanged
    assert get_shortish_repr(ShortAddr(), normalize=True) == "foo at 0x12"

    class MultiAddr:
        def __repr__(self):
            return "<A at 0xABCDEF> and <B at 0x123456>"

    assert get_shortish_repr(MultiAddr(), normalize=True) == "<A> and <B>"

    class MultiLine:
        def __repr__(self):
            return "<Multi\nLine at 0xABCDEF1234>"

    # newlines stripped before normalize, then address removed
    result = get_shortish_repr(MultiLine(), normalize=True)
    assert "\n" not in result
    assert result == "<MultiLine>"
