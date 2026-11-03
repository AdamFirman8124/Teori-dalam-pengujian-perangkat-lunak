# file: project/pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

from pysnooper.utils import DEFAULT_REPR_RE, normalize_repr


def test_normalize_repr_removes_memory_address():
    """A default repr containing an address has the address stripped."""
    item_repr = '<Foo object at 0x7f8a2b3c4d5e>'
    result = normalize_repr(item_repr)
    assert result == '<Foo object>'


def test_normalize_repr_without_address_is_unchanged():
    """A repr without an address passes through untouched."""
    item_repr = '<Foo object>'
    assert normalize_repr(item_repr) == '<Foo object>'


def test_normalize_repr_removes_all_addresses():
    """Every address occurrence is removed, not just the first one."""
    item_repr = '[<A object at 0xdeadbeef>, <B object at 0x12345678>]'
    assert normalize_repr(item_repr) == '[<A object>, <B object>]'


def test_normalize_repr_requires_at_least_four_hex_digits():
    """The pattern needs at least 4 hex digits; shorter ones are kept."""
    item_repr = '<Foo object at 0x123>'
    assert normalize_repr(item_repr) == '<Foo object at 0x123>'


def test_normalize_repr_accepts_uppercase_hex_digits():
    """Hex digits may be uppercase (the 0x prefix must be lowercase)."""
    item_repr = '<Foo object at 0xABCDEF01>'
    assert normalize_repr(item_repr) == '<Foo object>'


def test_normalize_repr_ignores_hex_without_at_prefix():
    """Hex numbers not preceded by ' at ' are left alone."""
    item_repr = 'value 0x1234abcd'
    assert normalize_repr(item_repr) == 'value 0x1234abcd'


def test_normalize_repr_on_real_object_repr():
    """Works on the default repr of an actual object instance."""

    class Foo:
        pass

    item_repr = repr(Foo())
    # Precondition: the default repr really contains a memory address.
    assert DEFAULT_REPR_RE.search(item_repr)
    result = normalize_repr(item_repr)
    assert ' at 0x' not in result
    assert result == item_repr.split(' at 0x')[0] + '>'
