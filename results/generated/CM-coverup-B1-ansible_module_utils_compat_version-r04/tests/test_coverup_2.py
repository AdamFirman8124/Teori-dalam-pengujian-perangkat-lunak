# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

from ansible.module_utils.compat.version import Version


class _DummyVersion(Version):
    """Concrete subclass to exercise Version base-class logic."""

    def parse(self, vstring):
        self.vstring = vstring

    def __str__(self):
        return getattr(self, "vstring", "")

    def _cmp(self, other):
        if not isinstance(other, _DummyVersion):
            return NotImplemented
        if self.vstring == other.vstring:
            return 0
        return -1 if self.vstring < other.vstring else 1


def test_init_with_vstring_calls_parse():
    v = _DummyVersion("1.0")
    assert getattr(v, "vstring", None) == "1.0"


def test_init_without_vstring_skips_parse():
    v = _DummyVersion()
    assert getattr(v, "vstring", None) in (None, "")
    v2 = _DummyVersion(None)
    assert getattr(v2, "vstring", None) in (None, "")


def test_init_with_empty_string_skips_parse():
    v = _DummyVersion("")
    assert getattr(v, "vstring", None) in (None, "")


def test_repr_uses_classname_and_str():
    v = _DummyVersion("1.2")
    assert repr(v) == "%s ('%s')" % (_DummyVersion.__name__, str(v))
    assert repr(v) == "_DummyVersion ('1.2')"


def test_eq_equal_and_not_equal():
    a = _DummyVersion("1.0")
    b = _DummyVersion("1.0")
    c = _DummyVersion("2.0")
    assert (a == b) is True
    assert a.__eq__(b) is True
    assert (a == c) is False
    assert a.__eq__(c) is False


def test_eq_not_implemented():
    a = _DummyVersion("1.0")
    assert a.__eq__("1.0") is NotImplemented
    assert a.__eq__(object()) is NotImplemented


def test_lt():
    a = _DummyVersion("1.0")
    b = _DummyVersion("2.0")
    assert (a < b) is True
    assert a.__lt__(b) is True
    assert (b < a) is False
    assert b.__lt__(a) is False
    assert (a < _DummyVersion("1.0")) is False


def test_lt_not_implemented():
    a = _DummyVersion("1.0")
    assert a.__lt__("2.0") is NotImplemented
    assert a.__lt__(object()) is NotImplemented


def test_le():
    a = _DummyVersion("1.0")
    b = _DummyVersion("1.0")
    c = _DummyVersion("2.0")
    assert (a <= b) is True
    assert a.__le__(b) is True
    assert (a <= c) is True
    assert (c <= a) is False
    assert c.__le__(a) is False


def test_le_not_implemented():
    a = _DummyVersion("1.0")
    assert a.__le__("1.0") is NotImplemented
    assert a.__le__(object()) is NotImplemented


def test_gt():
    a = _DummyVersion("1.0")
    b = _DummyVersion("2.0")
    assert (b > a) is True
    assert b.__gt__(a) is True
    assert (a > b) is False
    assert a.__gt__(b) is False
    assert (a > _DummyVersion("1.0")) is False


def test_gt_not_implemented():
    a = _DummyVersion("1.0")
    assert a.__gt__("1.0") is NotImplemented
    assert a.__gt__(object()) is NotImplemented


def test_ge():
    a = _DummyVersion("1.0")
    b = _DummyVersion("1.0")
    c = _DummyVersion("2.0")
    assert (a >= b) is True
    assert a.__ge__(b) is True
    assert (c >= a) is True
    assert (a >= c) is False
    assert a.__ge__(c) is False


def test_ge_not_implemented():
    a = _DummyVersion("1.0")
    assert a.__ge__("1.0") is NotImplemented
    assert a.__ge__(object()) is NotImplemented
