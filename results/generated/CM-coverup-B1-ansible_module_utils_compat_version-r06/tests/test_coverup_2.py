# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

from ansible.module_utils.compat.version import Version


def test_version_initialization_and_repr():
    class ParsedVersion(Version):
        def parse(self, vstring):
            self.parse_arguments = getattr(self, "parse_arguments", [])
            self.parse_arguments.append(vstring)
            self.value = vstring

        def __str__(self):
            return self.value

    version = ParsedVersion("1.2.3")
    empty_version = ParsedVersion("")
    unspecified_version = ParsedVersion()

    assert version.parse_arguments == ["1.2.3"]
    assert version.value == "1.2.3"
    assert repr(version) == "ParsedVersion ('1.2.3')"
    assert not hasattr(empty_version, "parse_arguments")
    assert not hasattr(unspecified_version, "parse_arguments")


def test_version_rich_comparisons_for_supported_values():
    class ComparableVersion(Version):
        def __init__(self):
            self.compared_with = []

        def _cmp(self, other):
            self.compared_with.append(other)
            return other

    cases = (
        ("__eq__", 0, True, 1, False),
        ("__lt__", -1, True, 0, False),
        ("__le__", 0, True, 1, False),
        ("__gt__", 1, True, 0, False),
        ("__ge__", 0, True, -1, False),
    )

    for method_name, true_value, true_result, false_value, false_result in cases:
        version = ComparableVersion()
        method = getattr(Version, method_name)

        assert method(version, true_value) is true_result
        assert method(version, false_value) is false_result
        assert version.compared_with == [true_value, false_value]


def test_version_rich_comparisons_propagate_not_implemented():
    class UnsupportedVersion(Version):
        def __init__(self):
            self.compared_with = []

        def _cmp(self, other):
            self.compared_with.append(other)
            return NotImplemented

    for method_name in ("__eq__", "__lt__", "__le__", "__gt__", "__ge__"):
        version = UnsupportedVersion()
        method = getattr(Version, method_name)
        operand = object()

        assert method(version, operand) is NotImplemented
        assert version.compared_with == [operand]
