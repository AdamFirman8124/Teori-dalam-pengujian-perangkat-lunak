# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion, StrictVersion


def test_cmp_with_string():
    assert StrictVersion('1.0') == '1.0'
    assert StrictVersion('1.0') < '1.1'
    assert StrictVersion('1.1') > '1.0'
    assert StrictVersion('1.0a1') < '1.0'
    assert StrictVersion('1.0') > '1.0a1'


def test_cmp_with_non_strict_version_returns_notimplemented():
    assert StrictVersion('1.0')._cmp(42) is NotImplemented
    assert StrictVersion('1.0')._cmp(LooseVersion('1.0')) is NotImplemented


def test_cmp_numeric_versions_differ():
    assert StrictVersion('1.0')._cmp(StrictVersion('1.1')) == -1
    assert StrictVersion('1.1')._cmp(StrictVersion('1.0')) == 1
    assert StrictVersion('1.0') < StrictVersion('1.1')
    assert StrictVersion('1.1') > StrictVersion('1.0')


def test_cmp_equal_numeric_no_prerelease():
    assert StrictVersion('1.0')._cmp(StrictVersion('1.0.0')) == 0
    assert StrictVersion('1.0') == StrictVersion('1.0.0')


def test_cmp_prerelease_vs_release():
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0')) == -1
    assert StrictVersion('1.0')._cmp(StrictVersion('1.0a1')) == 1
    assert StrictVersion('1.0a1') < StrictVersion('1.0')
    assert StrictVersion('1.0') > StrictVersion('1.0a1')


def test_cmp_both_prerelease():
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0a1')) == 0
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0b1')) == -1
    assert StrictVersion('1.0b1')._cmp(StrictVersion('1.0a1')) == 1
    assert StrictVersion('1.0a1') == StrictVersion('1.0a1')
    assert StrictVersion('1.0a1') < StrictVersion('1.0b1')
    assert StrictVersion('1.0b1') > StrictVersion('1.0a1')


class _Toggle:
    """Truthiness source that yields a fixed sequence of booleans."""

    def __init__(self, values):
        self._values = iter(values)

    def __bool__(self):
        return next(self._values)


def test_cmp_unreachable_else_raises_assertion_error(monkeypatch):
    left = StrictVersion('1.0')
    right = StrictVersion('1.0')
    # Force every branch condition to evaluate false so the final
    # "never get here" AssertionError is reached.
    monkeypatch.setattr(left, 'prerelease', _Toggle([True, False, True, False]))
    monkeypatch.setattr(right, 'prerelease', _Toggle([False, True, False, False]))
    with pytest.raises(AssertionError, match='never get here'):
        left._cmp(right)
