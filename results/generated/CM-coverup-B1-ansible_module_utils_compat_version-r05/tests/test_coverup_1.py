# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_cmp_converts_string_and_rejects_unsupported_type():
    version = StrictVersion("1.0")

    assert version._cmp("1.0") == 0
    assert version._cmp(object()) is NotImplemented


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        ("1.0", "2.0", -1),
        ("2.0", "1.0", 1),
        ("1.0", "1.0", 0),
        ("1.0a1", "1.0", -1),
        ("1.0", "1.0a1", 1),
        ("1.0a1", "1.0a1", 0),
        ("1.0a1", "1.0a2", -1),
        ("1.0b1", "1.0a2", 1),
    ],
)
def test_cmp_covers_numeric_and_prerelease_ordering(left, right, expected):
    left_version = StrictVersion(left)
    right_version = StrictVersion(right)

    assert left_version._cmp(right_version) == expected


def test_cmp_defensive_unreachable_branch():
    class ChangingTruthValue:
        def __init__(self):
            self.results = iter((True, True, True, False))
            self.calls = 0

        def __bool__(self):
            self.calls += 1
            return next(self.results)

    left = StrictVersion("1.0a1")
    right = StrictVersion("1.0a1")
    changing_prerelease = ChangingTruthValue()
    left.prerelease = changing_prerelease

    with pytest.raises(AssertionError, match="never get here"):
        left._cmp(right)

    assert changing_prerelease.calls == 4
