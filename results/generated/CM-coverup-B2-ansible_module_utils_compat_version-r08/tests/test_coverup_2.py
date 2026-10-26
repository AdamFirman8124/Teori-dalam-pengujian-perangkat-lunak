# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion, Version


class _NotImplVersion(Version):
    """Concrete Version whose _cmp always returns NotImplemented."""

    def parse(self, vstring):
        self.parsed = vstring

    def _cmp(self, other):
        return NotImplemented


class _FixedVersion(Version):
    """Concrete Version whose _cmp returns a fixed value."""

    def __init__(self, result, vstring=None):
        self.result = result
        super().__init__(vstring)

    def parse(self, vstring):
        self.parsed = vstring

    def _cmp(self, other):
        return self.result


def test_init_with_vstring_calls_parse():
    v = _NotImplVersion("1.2.3")
    assert v.parsed == "1.2.3"


def test_init_without_vstring_does_not_parse():
    v = _NotImplVersion()
    assert not hasattr(v, "parsed")


def test_repr():
    v = StrictVersion("1.2.3")
    assert repr(v) == "StrictVersion ('1.2.3')"


def test_eq_not_implemented():
    v = _NotImplVersion()
    assert v.__eq__(object()) is NotImplemented


def test_lt_not_implemented():
    v = _NotImplVersion()
    assert v.__lt__(object()) is NotImplemented


def test_le_not_implemented():
    v = _NotImplVersion()
    assert v.__le__(object()) is NotImplemented


def test_gt_not_implemented():
    v = _NotImplVersion()
    assert v.__gt__(object()) is NotImplemented


def test_ge_not_implemented():
    v = _NotImplVersion()
    assert v.__ge__(object()) is NotImplemented


@pytest.mark.parametrize(
    "result, eq, lt, le, gt, ge",
    [
        (-1, False, True, True, False, False),
        (0, True, False, True, False, True),
        (1, False, False, False, True, True),
    ],
)
def test_rich_comparisons_positive_paths(result, eq, lt, le, gt, ge):
    v = _FixedVersion(result)
    other = object()
    assert v.__eq__(other) is eq
    assert v.__lt__(other) is lt
    assert v.__le__(other) is le
    assert v.__gt__(other) is gt
    assert v.__ge__(other) is ge


def test_rich_comparisons_with_real_versions():
    low = StrictVersion("1.0")
    high = StrictVersion("2.0")
    assert low.__eq__(high) is False
    assert low.__lt__(high) is True
    assert low.__le__(high) is True
    assert low.__gt__(high) is False
    assert low.__ge__(high) is False
    assert low.__eq__(StrictVersion("1.0")) is True
    assert low.__le__(StrictVersion("1.0")) is True
    assert low.__ge__(StrictVersion("1.0")) is True
