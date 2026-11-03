# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

import pytest

from pysnooper import utils


def test_get_shortish_repr_basic():
    """Lines 68-70, 73, 78: default repr is used, newlines stripped, returned."""
    result = utils.get_shortish_repr([1, 2, 3])
    assert result == '[1, 2, 3]'


def test_get_shortish_repr_strips_newlines():
    """Line 73: carriage returns and newlines are removed from the repr."""
    class MultiLine:
        def __repr__(self):
            return 'a\r\nb\nc'

    result = utils.get_shortish_repr(MultiLine())
    assert result == 'abc'
    assert '\r' not in result
    assert '\n' not in result


def test_get_shortish_repr_repr_failed():
    """Lines 71-72: a raising repr yields 'REPR FAILED'."""
    class Exploding:
        def __repr__(self):
            raise ValueError('boom')

    result = utils.get_shortish_repr(Exploding())
    assert result == 'REPR FAILED'


def test_get_shortish_repr_custom_repr_callable_condition():
    """Line 68: custom_repr with a callable condition overrides repr."""
    class Foo:
        def __repr__(self):
            return 'default repr'

    result = utils.get_shortish_repr(
        Foo(), custom_repr=((lambda x: True, lambda x: 'CUSTOM'),)
    )
    assert result == 'CUSTOM'


def test_get_shortish_repr_custom_repr_type_condition():
    """Line 68: custom_repr with a type condition overrides repr."""
    class Foo:
        def __repr__(self):
            return 'default repr'

    result = utils.get_shortish_repr(
        Foo(), custom_repr=((Foo, lambda x: 'TYPED'),)
    )
    assert result == 'TYPED'


def test_get_shortish_repr_custom_repr_not_matching():
    """Line 68: non-matching custom_repr falls back to the default repr."""
    class Foo:
        def __repr__(self):
            return 'default repr'

    class Bar:
        pass

    result = utils.get_shortish_repr(
        Foo(), custom_repr=((Bar, lambda x: 'TYPED'),)
    )
    assert result == 'default repr'


def test_get_shortish_repr_normalize():
    """Lines 74-75: normalize=True strips the memory address."""
    class Obj:
        def __repr__(self):
            return 'Obj object at 0xdeadbeef'

    result = utils.get_shortish_repr(Obj(), normalize=True)
    assert result == 'Obj object'
    assert '0x' not in result


def test_get_shortish_repr_no_normalize():
    """Branch: normalize=False keeps the memory address intact."""
    class Obj:
        def __repr__(self):
            return 'Obj object at 0xdeadbeef'

    result = utils.get_shortish_repr(Obj(), normalize=False)
    assert result == 'Obj object at 0xdeadbeef'


def test_get_shortish_repr_max_length():
    """Lines 76-77: truthy max_length truncates the repr."""
    class LongRepr:
        def __repr__(self):
            return 'a' * 100

    result = utils.get_shortish_repr(LongRepr(), max_length=10)
    # left = (10 - 3) // 2 == 3, right = 10 - 3 - 3 == 4
    assert result == 'aaa...aaaa'
    assert len(result) == 10


def test_get_shortish_repr_max_length_string_item():
    """Lines 76-77: truncating a plain string keeps its repr quotes."""
    result = utils.get_shortish_repr('a' * 100, max_length=10)
    # repr('a' * 100) == "'aaa...aaa'" (102 chars incl. quotes);
    # left = (10 - 3) // 2 == 3 -> "'aa", right = 10 - 3 - 3 == 4 -> "aaa'"
    assert result == "'aa...aaa'"
    assert len(result) == 10


def test_get_shortish_repr_max_length_not_exceeded():
    """Branch: max_length set but repr is short enough -> unchanged."""
    class ShortRepr:
        def __repr__(self):
            return 'short'

    result = utils.get_shortish_repr(ShortRepr(), max_length=100)
    assert result == 'short'


def test_get_shortish_repr_falsy_max_length():
    """Branch: falsy max_length (None or 0) skips truncation entirely."""
    class LongRepr:
        def __repr__(self):
            return 'x' * 50

    item = LongRepr()
    assert utils.get_shortish_repr(item, max_length=None) == 'x' * 50
    assert utils.get_shortish_repr(item, max_length=0) == 'x' * 50


def test_get_shortish_repr_all_features_combined():
    """Lines 68-78: custom repr, newline stripping, normalize and truncate."""
    class Obj:
        pass

    def custom_repr(_):
        return 'thing at 0x1234abcd\nsecond\rline, plus lots of padding text here'

    result = utils.get_shortish_repr(
        Obj(),
        custom_repr=((Obj, custom_repr),),
        max_length=20,
        normalize=True,
    )
    # After newline removal: 'thing at 0x1234abcdsecondline, plus lots of padding text here'
    # After normalization:   'thingsecondline, plus lots of padding text here'
    # After truncation (max_length=20): left=(20-3)//2=8, right=20-3-8=9
    assert result == 'thingsec...text here'
    assert len(result) == 20
    assert '0x' not in result
    assert '\n' not in result
    assert '\r' not in result
