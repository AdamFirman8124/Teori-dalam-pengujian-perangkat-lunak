# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_cmp_accepts_string_version():
    version = StrictVersion("1.2.3")

    assert version._cmp("1.2.3") == 0


def test_cmp_returns_not_implemented_for_unsupported_type():
    version = StrictVersion("1.2.3")

    assert version._cmp(object()) is NotImplemented


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        ("1.2.2", "1.2.3", -1),
        ("1.2.4", "1.2.3", 1),
        ("1.2.3", "1.2.3", 0),
        ("1.2.3a1", "1.2.3", -1),
        ("1.2.3", "1.2.3a1", 1),
        ("1.2.3a1", "1.2.3a1", 0),
        ("1.2.3a1", "1.2.3a2", -1),
        ("1.2.3b1", "1.2.3a2", 1),
    ],
)
def test_cmp_covers_numeric_and_prerelease_ordering(left, right, expected):
    assert StrictVersion(left)._cmp(StrictVersion(right)) == expected


def test_cmp_rejects_logically_inconsistent_prerelease_state():
    class AlternatingTruth:
        def __init__(self):
            self.calls = 0

        def __bool__(self):
            self.calls += 1
            return self.calls % 2 == 1

    left = StrictVersion("1.2.3")
    right = StrictVersion("1.2.3")
    alternating = AlternatingTruth()
    left.prerelease = alternating

    with pytest.raises(AssertionError, match="never get here"):
        left._cmp(right)

    assert alternating.calls == 4
