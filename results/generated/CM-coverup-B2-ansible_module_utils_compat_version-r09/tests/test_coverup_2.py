# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

"""Coverage tests for ansible.module_utils.compat.version.Version.

The base ``Version`` class is abstract: ``LooseVersion`` overrides both
``__init__`` and ``__repr__``, so a small local subclass is used to drive the
base-class implementations of those methods.  All rich comparisons are
inherited from ``Version`` by ``LooseVersion``, so they are exercised through
both classes, including the ``NotImplemented`` propagation branches
(``LooseVersion._cmp`` returns ``NotImplemented`` for unsupported operand
types).

No global state is modified by these tests, so no cleanup is required.
"""

from ansible.module_utils.compat.version import LooseVersion, Version


class DummyVersion(Version):
    """Minimal concrete Version used to exercise the abstract base class.

    It deliberately does *not* override ``__init__`` or ``__repr__`` so that
    ``Version.__init__`` and ``Version.__repr__`` themselves run, and its
    ``_cmp`` returns ``NotImplemented`` for operands it cannot handle so the
    base-class rich comparators propagate it.
    """

    def parse(self, vstring):
        self.version = tuple(int(part) for part in vstring.split("."))

    def __str__(self):
        return ".".join(str(part) for part in self.version)

    def _cmp(self, other):
        if isinstance(other, str):
            other = DummyVersion(other)
        if not isinstance(other, DummyVersion):
            return NotImplemented
        if self.version == other.version:
            return 0
        if self.version < other.version:
            return -1
        return 1


def test_version_init_with_vstring_calls_parse():
    v = DummyVersion("1.2.3")
    assert v.version == (1, 2, 3)


def test_version_init_without_vstring_skips_parse():
    # Falsy vstring (the default) must not invoke parse().
    assert not hasattr(DummyVersion(), "version")
    assert not hasattr(Version(), "version")


def test_version_repr():
    v = DummyVersion("1.2.3")
    assert repr(v) == "DummyVersion ('1.2.3')"


def test_version_eq():
    assert (DummyVersion("1.0") == DummyVersion("1.0")) is True
    assert (DummyVersion("1.0") == DummyVersion("2.0")) is False
    assert (DummyVersion("1.0") == "1.0") is True
    assert (DummyVersion("1.0") != DummyVersion("2.0")) is True
    # Unsupported operand type: _cmp returns NotImplemented, which __eq__
    # must propagate unchanged (checked via the dunder to bypass the
    # operator fallback machinery).
    assert DummyVersion("1.0").__eq__(object()) is NotImplemented


def test_version_lt():
    assert (DummyVersion("1.0") < DummyVersion("2.0")) is True
    assert (DummyVersion("2.0") < DummyVersion("1.0")) is False
    assert (DummyVersion("1.0") < DummyVersion("1.0")) is False
    assert DummyVersion("1.0").__lt__(object()) is NotImplemented


def test_version_le():
    assert (DummyVersion("1.0") <= DummyVersion("1.0")) is True
    assert (DummyVersion("1.0") <= DummyVersion("2.0")) is True
    assert (DummyVersion("2.0") <= DummyVersion("1.0")) is False
    assert DummyVersion("1.0").__le__(object()) is NotImplemented


def test_version_gt():
    assert (DummyVersion("2.0") > DummyVersion("1.0")) is True
    assert (DummyVersion("1.0") > DummyVersion("2.0")) is False
    assert (DummyVersion("1.0") > DummyVersion("1.0")) is False
    assert DummyVersion("1.0").__gt__(object()) is NotImplemented


def test_version_ge():
    assert (DummyVersion("1.0") >= DummyVersion("1.0")) is True
    assert (DummyVersion("2.0") >= DummyVersion("1.0")) is True
    assert (DummyVersion("1.0") >= DummyVersion("2.0")) is False
    assert DummyVersion("1.0").__ge__(object()) is NotImplemented


def test_looseversion_inherits_base_comparators():
    v = LooseVersion("1.2.3")
    assert v.version == [1, 2, 3]
    assert (v == LooseVersion("1.2.3")) is True
    assert (v < LooseVersion("1.3")) is True
    assert (v <= "1.2.3") is True
    assert (LooseVersion("2.0") > v) is True
    assert (v >= "1.3") is False


def test_looseversion_comparator_propagates_notimplemented():
    # LooseVersion._cmp returns NotImplemented for operands that are neither
    # str nor LooseVersion; the inherited base-class comparators must pass
    # that through unchanged.
    v = LooseVersion("1.0")
    assert v.__eq__(object()) is NotImplemented
    assert v.__lt__(object()) is NotImplemented
    assert v.__le__(object()) is NotImplemented
    assert v.__gt__(object()) is NotImplemented
    assert v.__ge__(object()) is NotImplemented
