# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

import pytest

from ansible.module_utils.compat.version import Version


class _DummyVersion(Version):
    """Minimal concrete Version subclass used to exercise the base class."""

    def parse(self, vstring):
        self.vstring = vstring
        self.value = int(vstring)

    def __str__(self):
        return self.vstring

    def _cmp(self, other):
        if isinstance(other, _DummyVersion):
            other_value = other.value
        elif isinstance(other, int):
            other_value = other
        else:
            return NotImplemented
        if self.value == other_value:
            return 0
        return -1 if self.value < other_value else 1


def test_init_parses_vstring():
    v = _DummyVersion("7")
    assert v.vstring == "7"
    assert v.value == 7


def test_init_without_vstring_skips_parse(monkeypatch):
    calls = []
    monkeypatch.setattr(_DummyVersion, "parse", lambda self, s: calls.append(s))
    v = _DummyVersion()
    assert calls == []
    assert not hasattr(v, "value")


def test_repr():
    assert repr(_DummyVersion("3")) == "_DummyVersion ('3')"


def test_eq():
    assert _DummyVersion("2") == _DummyVersion("2")
    assert not (_DummyVersion("2") == _DummyVersion("3"))
    assert _DummyVersion.__eq__(_DummyVersion("2"), object()) is NotImplemented


def test_lt():
    assert _DummyVersion("2") < _DummyVersion("3")
    assert not (_DummyVersion("3") < _DummyVersion("2"))
    assert _DummyVersion.__lt__(_DummyVersion("2"), object()) is NotImplemented


def test_le():
    assert _DummyVersion("2") <= _DummyVersion("2")
    assert _DummyVersion("2") <= _DummyVersion("3")
    assert not (_DummyVersion("3") <= _DummyVersion("2"))
    assert _DummyVersion.__le__(_DummyVersion("2"), object()) is NotImplemented


def test_gt():
    assert _DummyVersion("3") > _DummyVersion("2")
    assert not (_DummyVersion("2") > _DummyVersion("3"))
    assert _DummyVersion.__gt__(_DummyVersion("2"), object()) is NotImplemented


def test_ge():
    assert _DummyVersion("2") >= _DummyVersion("2")
    assert _DummyVersion("3") >= _DummyVersion("2")
    assert not (_DummyVersion("2") >= _DummyVersion("3"))
    assert _DummyVersion.__ge__(_DummyVersion("2"), object()) is NotImplemented


def test_comparisons_against_int():
    v = _DummyVersion("5")
    assert v == 5
    assert v <= 5
    assert v >= 5
    assert not (v < 5)
    assert not (v > 5)
    assert v > 4
    assert v < 6
