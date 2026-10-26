# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

from ansible.module_utils.compat.version import Version


def test_version_init_with_vstring_calls_parse():
    class V(Version):
        def __init__(self, vstring=None):
            self.parse_calls = []
            super().__init__(vstring)

        def parse(self, vstring):
            self.parse_calls.append(vstring)

        def __str__(self):
            return "1.0"

        def _cmp(self, other):
            return 0

    v = V("1.2.3")
    assert v.parse_calls == ["1.2.3"]


def test_version_init_without_vstring_skips_parse():
    class V(Version):
        def __init__(self, vstring=None):
            self.parse_called = False
            super().__init__(vstring)

        def parse(self, vstring):
            self.parse_called = True

        def __str__(self):
            return "1.0"

        def _cmp(self, other):
            return 0

    v1 = V()
    assert v1.parse_called is False
    v2 = V(None)
    assert v2.parse_called is False
    v3 = V("")
    assert v3.parse_called is False


def test_version_repr():
    class V(Version):
        def __str__(self):
            return "1.2.3"

        def _cmp(self, other):
            return 0

    v = V()
    assert repr(v) == "V ('1.2.3')"
    assert Version.__repr__(v) == "V ('1.2.3')"


def test_version_eq():
    class V(Version):
        def __init__(self, val):
            self.val = val

        def __str__(self):
            return "1.0"

        def _cmp(self, other):
            return self.val

    assert V(0).__eq__(object()) is True
    assert V(0) == V(0)
    assert V(1).__eq__(object()) is False
    assert V(-1).__eq__(object()) is False
    assert (V(1) == V(2)) is False
    assert V(NotImplemented).__eq__(object()) is NotImplemented


def test_version_lt():
    class V(Version):
        def __init__(self, val):
            self.val = val

        def __str__(self):
            return "1.0"

        def _cmp(self, other):
            return self.val

    assert V(-1).__lt__(object()) is True
    assert (V(-1) < V(0)) is True
    assert V(0).__lt__(object()) is False
    assert V(1).__lt__(object()) is False
    assert (V(1) < V(0)) is False
    assert V(NotImplemented).__lt__(object()) is NotImplemented


def test_version_le():
    class V(Version):
        def __init__(self, val):
            self.val = val

        def __str__(self):
            return "1.0"

        def _cmp(self, other):
            return self.val

    assert V(-1).__le__(object()) is True
    assert V(0).__le__(object()) is True
    assert (V(0) <= V(0)) is True
    assert V(1).__le__(object()) is False
    assert (V(1) <= V(0)) is False
    assert V(NotImplemented).__le__(object()) is NotImplemented


def test_version_gt():
    class V(Version):
        def __init__(self, val):
            self.val = val

        def __str__(self):
            return "1.0"

        def _cmp(self, other):
            return self.val

    assert V(1).__gt__(object()) is True
    assert (V(1) > V(0)) is True
    assert V(0).__gt__(object()) is False
    assert V(-1).__gt__(object()) is False
    assert (V(-1) > V(0)) is False
    assert V(NotImplemented).__gt__(object()) is NotImplemented


def test_version_ge():
    class V(Version):
        def __init__(self, val):
            self.val = val

        def __str__(self):
            return "1.0"

        def _cmp(self, other):
            return self.val

    assert V(1).__ge__(object()) is True
    assert V(0).__ge__(object()) is True
    assert (V(0) >= V(0)) is True
    assert V(-1).__ge__(object()) is False
    assert (V(-1) >= V(0)) is False
    assert V(NotImplemented).__ge__(object()) is NotImplemented
