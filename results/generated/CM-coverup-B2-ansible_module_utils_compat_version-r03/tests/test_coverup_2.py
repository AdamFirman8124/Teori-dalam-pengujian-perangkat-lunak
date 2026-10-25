# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

from ansible.module_utils.compat.version import Version


def test_version_initialization_and_repr():
    parsed_values = []

    class ConcreteVersion(Version):
        def parse(self, vstring):
            parsed_values.append(vstring)
            self.value = vstring

        def __str__(self):
            return self.value

    version = ConcreteVersion("1.2.3")

    assert parsed_values == ["1.2.3"]
    assert repr(version) == "ConcreteVersion ('1.2.3')"

    empty_version = ConcreteVersion("")

    assert parsed_values == ["1.2.3"]
    assert not hasattr(empty_version, "value")


def test_version_rich_comparisons_cover_all_results():
    class ComparableVersion(Version):
        def __init__(self):
            super().__init__()
            self.compared_with = []

        def _cmp(self, other):
            self.compared_with.append(other)
            return other

    version = ComparableVersion()
    expectations = {
        "__eq__": {-1: False, 0: True, 1: False},
        "__lt__": {-1: True, 0: False, 1: False},
        "__le__": {-1: True, 0: True, 1: False},
        "__gt__": {-1: False, 0: False, 1: True},
        "__ge__": {-1: False, 0: True, 1: True},
    }

    for method_name, results in expectations.items():
        method = getattr(version, method_name)

        assert method(NotImplemented) is NotImplemented
        for comparison_result, expected in results.items():
            assert method(comparison_result) is expected

    assert version.compared_with == [
        value
        for _ in expectations
        for value in (NotImplemented, -1, 0, 1)
    ]
