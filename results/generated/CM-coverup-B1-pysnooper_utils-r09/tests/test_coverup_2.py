# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

import re

from pysnooper.utils import get_shortish_repr


def test_get_shortish_repr_basic():
    result = get_shortish_repr('hello')
    assert result == "'hello'"


def test_get_shortish_repr_strips_newlines_and_carriage_returns():
    class Weird:
        def __repr__(self):
            return 'line1\r\nline2\nline3\r'

    result = get_shortish_repr(Weird())
    assert result == 'line1line2line3'
    assert '\n' not in result
    assert '\r' not in result


def test_get_shortish_repr_exception_path():
    class Exploding:
        def __repr__(self):
            raise ValueError('boom')

    result = get_shortish_repr(Exploding())
    assert result == 'REPR FAILED'


def test_get_shortish_repr_normalize():
    item = object()
    result = get_shortish_repr(item, normalize=True)
    assert result == re.sub(r' at 0x[a-f0-9A-F]{4,}', '', repr(item))
    assert result == '<object object>'
    assert '0x' not in result


def test_get_shortish_repr_normalize_false_keeps_address():
    item = object()
    result = get_shortish_repr(item, normalize=False)
    assert result == repr(item)
    assert '0x' in result


def test_get_shortish_repr_max_length_truncates():
    result = get_shortish_repr('abcdefghijklmnopqrstuvwxyz', max_length=10)
    # repr is "'abcdefghijklmnopqrstuvwxyz'" (28 chars), truncated to 10:
    # left=3, right=4 -> "'ab" + "..." + "xyz'"
    assert result == "'ab...xyz'"
    assert len(result) == 10


def test_get_shortish_repr_max_length_no_truncation_needed():
    result = get_shortish_repr('short', max_length=100)
    assert result == "'short'"


def test_get_shortish_repr_max_length_falsy_skips_truncation():
    result = get_shortish_repr('short', max_length=None)
    assert result == "'short'"
    result_zero = get_shortish_repr('short', max_length=0)
    assert result_zero == "'short'"


def test_get_shortish_repr_exception_with_normalize_and_max_length():
    class Exploding:
        def __repr__(self):
            raise RuntimeError('nope')

    result = get_shortish_repr(Exploding(), max_length=5, normalize=True)
    # 'REPR FAILED' normalized is unchanged, truncated to 5: 'R' + '...' + 'D'
    assert result == 'R...D'
    assert len(result) == 5


def test_get_shortish_repr_custom_repr_used():
    class Foo:
        def __repr__(self):
            return 'boring default'

    def custom_action(x):
        return 'custom foo repr'

    result = get_shortish_repr(Foo(), custom_repr=((Foo, custom_action),))
    assert result == 'custom foo repr'


def test_get_shortish_repr_custom_repr_exception_still_caught():
    class Bar:
        pass

    def bad_action(x):
        raise KeyError('custom repr failed')

    result = get_shortish_repr(Bar(), custom_repr=((Bar, bad_action),))
    assert result == 'REPR FAILED'


def test_get_shortish_repr_combined_newlines_normalize_truncate():
    class Multi:
        def __repr__(self):
            return 'aaa\nbbb at 0xdeadbeef ccc\nddd'

    result = get_shortish_repr(Multi(), max_length=12, normalize=True)
    # strip newlines -> 'aaabbb at 0xdeadbeef cccddd'
    # normalize removes ' at 0xdeadbeef' -> 'aaabbb cccddd' (len 13)
    # truncate to 12: left=4, right=5 -> 'aaab' + '...' + 'ccddd'
    assert result == 'aaab...ccddd'
    assert len(result) == 12
    assert '\n' not in result
    assert '0x' not in result
