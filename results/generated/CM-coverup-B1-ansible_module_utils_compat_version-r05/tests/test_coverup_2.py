# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

from ansible.module_utils.compat.version import Version


def test_version_init_and_repr():
    class StubVersion(Version):
        def parse(self, vstring):
            self.parsed = vstring

        def __str__(self):
            return self.parsed

    version = StubVersion("1.2.3")
    assert version.parsed == "1.2.3"
    assert repr(version) == "StubVersion ('1.2.3')"

    empty_version = StubVersion("")
    assert not hasattr(empty_version, "parsed")


def test_version_comparisons():
    class StubVersion(Version):
        def _cmp(self, other):
            return other

    version = StubVersion()
    cases = (
        (version.__eq__, 0, True),
        (version.__eq__, 1, False),
        (version.__lt__, -1, True),
        (version.__lt__, 0, False),
        (version.__le__, 0, True),
        (version.__le__, 1, False),
        (version.__gt__, 1, True),
        (version.__gt__, 0, False),
        (version.__ge__, 0, True),
        (version.__ge__, -1, False),
    )

    for comparison_method, comparison_result, expected in cases:
        assert comparison_method(comparison_result) is expected


def test_version_comparisons_propagate_not_implemented():
    class StubVersion(Version):
        def _cmp(self, other):
            return NotImplemented

    version = StubVersion()

    for comparison_method in (
        version.__eq__,
        version.__lt__,
        version.__le__,
        version.__gt__,
        version.__ge__,
    ):
        assert comparison_method(object()) is NotImplemented
