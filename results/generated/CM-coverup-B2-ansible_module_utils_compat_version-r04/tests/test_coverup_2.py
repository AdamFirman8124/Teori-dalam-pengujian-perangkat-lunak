# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

from ansible.module_utils.compat.version import Version


def test_version_init_and_repr():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.value = vstring

        def __str__(self):
            return self.value

    unparsed = DummyVersion()
    assert not hasattr(unparsed, "value")

    version = DummyVersion("1.2.3")
    assert version.value == "1.2.3"
    assert repr(version) == "DummyVersion ('1.2.3')"


def test_version_rich_comparisons():
    class DummyVersion(Version):
        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    version = DummyVersion()
    other = object()

    cases = (
        (Version.__eq__, ((NotImplemented, NotImplemented), (0, True), (1, False))),
        (Version.__lt__, ((NotImplemented, NotImplemented), (-1, True), (0, False))),
        (Version.__le__, ((NotImplemented, NotImplemented), (0, True), (1, False))),
        (Version.__gt__, ((NotImplemented, NotImplemented), (1, True), (0, False))),
        (Version.__ge__, ((NotImplemented, NotImplemented), (0, True), (-1, False))),
    )

    for comparison_method, results in cases:
        for comparison_result, expected in results:
            version.comparison_result = comparison_result
            version.compared_with = None

            actual = comparison_method(version, other)

            assert actual is expected
            assert version.compared_with is other
