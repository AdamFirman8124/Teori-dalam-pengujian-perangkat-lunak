# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

"""Tests for pysnooper.utils.get_shortish_repr (lines 68-78).

These tests are pure (no files, no global state, no monkeypatching needed),
so there is no state to clean up between tests.
"""

from pysnooper import utils


class Unrepresentable(object):
    def __repr__(self):
        raise ValueError('nope')


class Custom(object):
    pass


class MultiLine(object):
    def __repr__(self):
        return 'line1\rline2\nline3\r\n'


def test_get_shortish_repr_basic():
    """Lines 68, 70, 73, 78: plain repr, no normalization, no truncation."""
    assert utils.get_shortish_repr('foo') == "'foo'"


def test_get_shortish_repr_removes_newlines():
    """Line 73: carriage returns and newlines are stripped from the repr."""
    result = utils.get_shortish_repr(MultiLine())
    assert result == 'line1line2line3'


def test_get_shortish_repr_custom_repr_type_condition():
    """Line 68: get_repr_function picks the custom repr for a matching type."""
    result = utils.get_shortish_repr(
        Custom(), custom_repr=((Custom, lambda x: 'CUSTOM!'),))
    assert result == 'CUSTOM!'


def test_get_shortish_repr_custom_repr_callable_condition():
    """Line 68: custom repr with a plain callable condition."""
    result = utils.get_shortish_repr(
        42, custom_repr=((lambda x: x == 42, lambda x: 'FORTY-TWO'),))
    assert result == 'FORTY-TWO'


def test_get_shortish_repr_custom_repr_not_matching():
    """Line 68: falls back to the builtin repr when no condition matches."""
    result = utils.get_shortish_repr(
        'hello', custom_repr=((Custom, lambda x: 'CUSTOM!'),))
    assert result == "'hello'"


def test_get_shortish_repr_failed_repr():
    """Lines 71-72: a raising repr yields the REPR FAILED placeholder."""
    assert utils.get_shortish_repr(Unrepresentable()) == 'REPR FAILED'


def test_get_shortish_repr_failed_repr_with_options():
    """Lines 71-72 combined with 74-77: failure path is still processed."""
    result = utils.get_shortish_repr(Unrepresentable(),
                                     max_length=5, normalize=True)
    assert result == 'R...D'


def test_get_shortish_repr_normalize():
    """Lines 74-75: memory addresses are removed when normalize is True."""
    result = utils.get_shortish_repr(Custom(), normalize=True)
    assert '0x' not in result
    assert ' at ' not in result
    assert result.endswith('Custom object>')


def test_get_shortish_repr_no_normalize():
    """Line 74 (False branch): address is kept when normalize is False."""
    result = utils.get_shortish_repr(Custom())
    assert '0x' in result


def test_get_shortish_repr_max_length():
    """Lines 76-77: long reprs are truncated to exactly max_length.

    Note: for a string item, the repr (including the surrounding quotes)
    is what gets truncated, so the expectation is computed from repr(s).
    """
    s = 'abcdefghij' * 10
    result = utils.get_shortish_repr(s, max_length=25)
    r = repr(s)
    assert result == r[:11] + '...' + r[-11:]
    assert len(result) == 25


def test_get_shortish_repr_max_length_not_needed():
    """Line 76: max_length set but the repr is already short enough."""
    assert utils.get_shortish_repr('short', max_length=100) == "'short'"


def test_get_shortish_repr_normalize_and_max_length():
    """Lines 74-77 combined: repr is normalized first, then truncated."""
    result = utils.get_shortish_repr(Custom(), normalize=True, max_length=20)
    assert '0x' not in result
    assert len(result) <= 20
    assert result == utils.truncate(utils.normalize_repr(repr(Custom())), 20)
