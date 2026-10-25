# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

from ansible.module_utils.compat.version import Version


def test_version_initialization_and_repr():
    class RecordingVersion(Version):
        def parse(self, vstring):
            self.parsed = vstring

        def __str__(self):
            return self.parsed

    version = RecordingVersion("1.2.3")

    assert version.parsed == "1.2.3"
    assert repr(version) == "RecordingVersion ('1.2.3')"

    empty_version = RecordingVersion("")
    assert not hasattr(empty_version, "parsed")

    none_version = RecordingVersion()
    assert not hasattr(none_version, "parsed")


def test_version_rich_comparison_methods():
    class ComparableVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    cases = (
        ("__eq__", 0, True),
        ("__eq__", 1, False),
        ("__eq__", NotImplemented, NotImplemented),
        ("__lt__", -1, True),
        ("__lt__", 0, False),
        ("__lt__", NotImplemented, NotImplemented),
        ("__le__", 0, True),
        ("__le__", 1, False),
        ("__le__", NotImplemented, NotImplemented),
        ("__gt__", 1, True),
        ("__gt__", 0, False),
        ("__gt__", NotImplemented, NotImplemented),
        ("__ge__", 0, True),
        ("__ge__", -1, False),
        ("__ge__", NotImplemented, NotImplemented),
    )

    for method_name, comparison_result, expected in cases:
        version = ComparableVersion(comparison_result)
        other = object()

        result = getattr(version, method_name)(other)

        assert result is expected
        assert version.compared_with is other
