# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

import pytest

from ansible.module_utils.compat.version import Version


class _DummyVersion(Version):
    """Minimal concrete Version for exercising the base class."""

    def parse(self, vstring):
        self.vstring = vstring

    def __str__(self):
        return self.vstring

    def _cmp(self, other):
        if not isinstance(other, _DummyVersion):
            return NotImplemented
        if self.vstring == other.vstring:
            return 0
        return -1 if self.vstring < other.vstring else 1


def test_init_with_vstring_calls_parse():
    v = _DummyVersion("1.2.3")
    assert v.vstring == "1.2.3"


def test_init_without_vstring_skips_parse():
    v = _DummyVersion()
    assert not hasattr(v, "vstring")


def test_repr():
    v = _DummyVersion("1.2.3")
    assert repr(v) == "_DummyVersion ('1.2.3')"


def test_eq_true():
    assert _DummyVersion("1.0") == _DummyVersion("1.0")


def test_eq_false():
    assert not (_DummyVersion("1.0") == _DummyVersion("2.0"))


def test_eq_not_implemented():
    assert _DummyVersion("1.0").__eq__(object()) is NotImplemented


def test_lt_true():
    assert _DummyVersion("1.0") < _DummyVersion("2.0")


def test_lt_false():
    assert not (_DummyVersion("2.0") < _DummyVersion("1.0"))


def test_lt_not_implemented():
    assert _DummyVersion("1.0").__lt__(object()) is NotImplemented


def test_le_true():
    assert _DummyVersion("1.0") <= _DummyVersion("1.0")
    assert _DummyVersion("1.0") <= _DummyVersion("2.0")


def test_le_false():
    assert not (_DummyVersion("2.0") <= _DummyVersion("1.0"))


def test_le_not_implemented():
    assert _DummyVersion("1.0").__le__(object()) is NotImplemented


def test_gt_true():
    assert _DummyVersion("2.0") > _DummyVersion("1.0")


def test_gt_false():
    assert not (_DummyVersion("1.0") > _DummyVersion("2.0"))


def test_gt_not_implemented():
    assert _DummyVersion("1.0").__gt__(object()) is NotImplemented


def test_ge_true():
    assert _DummyVersion("1.0") >= _DummyVersion("1.0")
    assert _DummyVersion("2.0") >= _DummyVersion("1.0")


def test_ge_false():
    assert not (_DummyVersion("1.0") >= _DummyVersion("2.0"))


def test_ge_not_implemented():
    assert _DummyVersion("1.0").__ge__(object()) is NotImplemented
