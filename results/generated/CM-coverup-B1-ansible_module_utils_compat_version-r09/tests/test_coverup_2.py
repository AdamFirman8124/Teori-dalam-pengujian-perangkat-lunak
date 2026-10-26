# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

from ansible.module_utils.compat.version import Version


def test_version_initialization_and_repr():
    class RecordingVersion(Version):
        def parse(self, vstring):
            self.parsed = vstring

        def __str__(self):
            return getattr(self, "parsed", "unparsed")

    parsed_version = RecordingVersion("1.2.3")
    assert parsed_version.parsed == "1.2.3"
    assert repr(parsed_version) == "RecordingVersion ('1.2.3')"

    unparsed_version = RecordingVersion("")
    assert not hasattr(unparsed_version, "parsed")
    assert repr(unparsed_version) == "RecordingVersion ('unparsed')"


def test_version_rich_comparisons_and_not_implemented():
    class ComparableVersion(Version):
        def _cmp(self, other):
            return other

    version = ComparableVersion()

    assert version.__eq__(0) is True
    assert version.__eq__(1) is False
    assert version.__eq__(NotImplemented) is NotImplemented

    assert version.__lt__(-1) is True
    assert version.__lt__(0) is False
    assert version.__lt__(NotImplemented) is NotImplemented

    assert version.__le__(0) is True
    assert version.__le__(1) is False
    assert version.__le__(NotImplemented) is NotImplemented

    assert version.__gt__(1) is True
    assert version.__gt__(0) is False
    assert version.__gt__(NotImplemented) is NotImplemented

    assert version.__ge__(0) is True
    assert version.__ge__(-1) is False
    assert version.__ge__(NotImplemented) is NotImplemented
