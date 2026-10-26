# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

from ansible.module_utils.compat.version import Version


class _DummyVersion(Version):
    def parse(self, vstring):
        self.vstring = vstring

    def __str__(self):
        return getattr(self, "vstring", "dummy")

    def _cmp(self, other):
        return getattr(self, "_cmp_value", 0)


def test_version_init_with_vstring():
    v = _DummyVersion("1.2.3")
    assert getattr(v, "vstring", None) == "1.2.3"
    assert str(v) == "1.2.3"


def test_version_init_without_vstring():
    v_none = _DummyVersion(None)
    assert getattr(v_none, "vstring", None) is None
    v_default = _DummyVersion()
    assert getattr(v_default, "vstring", None) is None
    v_empty = _DummyVersion("")
    assert getattr(v_empty, "vstring", None) is None


def test_version_repr():
    v = _DummyVersion("1.2.3")
    assert repr(v) == "%s ('%s')" % (_DummyVersion.__name__, "1.2.3")
    v2 = _DummyVersion()
    assert repr(v2) == "%s ('%s')" % (_DummyVersion.__name__, "dummy")


def test_version_eq_true():
    v1 = _DummyVersion("1.0")
    v1._cmp_value = 0
    v2 = _DummyVersion("1.0")
    v2._cmp_value = 0
    assert (v1 == v2) is True
    assert (v1.__eq__(v2)) is True


def test_version_eq_false():
    v1 = _DummyVersion("1.0")
    v1._cmp_value = 1
    v2 = _DummyVersion("2.0")
    assert (v1 == v2) is False


def test_version_eq_notimplemented():
    v = _DummyVersion("1.0")
    v._cmp_value = NotImplemented
    assert v.__eq__("other") is NotImplemented


def test_version_lt():
    v1 = _DummyVersion("1.0")
    v1._cmp_value = -1
    v2 = _DummyVersion("2.0")
    assert (v1 < v2) is True
    v1._cmp_value = 1
    assert (v1 < v2) is False


def test_version_lt_notimplemented():
    v = _DummyVersion("1.0")
    v._cmp_value = NotImplemented
    assert v.__lt__("other") is NotImplemented


def test_version_le():
    v1 = _DummyVersion("1.0")
    v1._cmp_value = 0
    v2 = _DummyVersion("1.0")
    assert (v1 <= v2) is True
    v1._cmp_value = -1
    assert (v1 <= v2) is True
    v1._cmp_value = 1
    assert (v1 <= v2) is False


def test_version_le_notimplemented():
    v = _DummyVersion("1.0")
    v._cmp_value = NotImplemented
    assert v.__le__("other") is NotImplemented


def test_version_gt():
    v1 = _DummyVersion("2.0")
    v1._cmp_value = 1
    v2 = _DummyVersion("1.0")
    assert (v1 > v2) is True
    v1._cmp_value = -1
    assert (v1 > v2) is False
    v1._cmp_value = 0
    assert (v1 > v2) is False


def test_version_gt_notimplemented():
    v = _DummyVersion("1.0")
    v._cmp_value = NotImplemented
    assert v.__gt__("other") is NotImplemented


def test_version_ge():
    v1 = _DummyVersion("1.0")
    v1._cmp_value = 0
    v2 = _DummyVersion("1.0")
    assert (v1 >= v2) is True
    v1._cmp_value = 1
    assert (v1 >= v2) is True
    v1._cmp_value = -1
    assert (v1 >= v2) is False


def test_version_ge_notimplemented():
    v = _DummyVersion("1.0")
    v._cmp_value = NotImplemented
    assert v.__ge__("other") is NotImplemented
