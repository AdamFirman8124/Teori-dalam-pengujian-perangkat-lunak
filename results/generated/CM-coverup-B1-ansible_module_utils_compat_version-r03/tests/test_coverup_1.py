# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


@pytest.mark.parametrize(
    "left,right,expected",
    [
        # version differs: _cmp via str-other branch and numeric compare
        ("1.0", "2.0", -1),
        ("2.0", "1.0", 1),
        ("0.9.6", "1.0", -1),
        ("1.0.1", "1.0", 1),
        # neither has prerelease
        ("1.0", "1.0", 0),
        ("1.0", "1.0.0", 0),
        # self has prerelease, other does not
        ("1.0a1", "1.0", -1),
        ("1.0b3", "1.0", -1),
        # self has no prerelease, other does
        ("1.0", "1.0a1", 1),
        ("1.0", "1.0b1", 1),
        # both have prerelease: equal / less / greater
        ("1.0a1", "1.0a1", 0),
        ("1.0b2", "1.0b2", 0),
        ("1.0a1", "1.0a2", -1),
        ("1.0a1", "1.0b1", -1),
        ("1.0a2", "1.0a1", 1),
        ("1.0b1", "1.0a1", 1),
    ],
)
def test_strictversion_cmp_with_str_other(left, right, expected):
    result = StrictVersion(left)._cmp(right)
    assert result == expected
    assert result in (-1, 0, 1)


@pytest.mark.parametrize(
    "left,right,expected",
    [
        ("1.0", "2.0", -1),
        ("2.0", "1.0", 1),
        ("1.0", "1.0", 0),
        ("1.0a1", "1.0", -1),
        ("1.0", "1.0a1", 1),
        ("1.0a1", "1.0a1", 0),
        ("1.0a1", "1.0b1", -1),
        ("1.0b1", "1.0a1", 1),
    ],
)
def test_strictversion_cmp_with_strictversion_other(left, right, expected):
    result = StrictVersion(left)._cmp(StrictVersion(right))
    assert result == expected


def test_strictversion_cmp_with_subclass_other():
    class SubStrictVersion(StrictVersion):
        pass

    assert StrictVersion("1.0")._cmp(SubStrictVersion("1.0")) == 0
    assert StrictVersion("1.0")._cmp(SubStrictVersion("2.0")) == -1
    assert StrictVersion("2.0")._cmp(SubStrictVersion("1.0")) == 1


@pytest.mark.parametrize("other", [123, 1.0, None, object(), ["1.0"], ("1", "0"), {"v": "1.0"}])
def test_strictversion_cmp_not_implemented_for_other_types(other):
    assert StrictVersion("1.0")._cmp(other) is NotImplemented


def test_strictversion_rich_comparison_with_str_and_other_types():
    assert StrictVersion("1.0") == "1.0"
    assert StrictVersion("1.0") == StrictVersion("1.0.0")
    assert StrictVersion("1.0a1") < StrictVersion("1.0")
    assert StrictVersion("1.0") > StrictVersion("1.0a1")
    assert StrictVersion("1.0a1") < "1.0b1"
    assert StrictVersion("2.0") > "1.0"
    assert StrictVersion("1.0") != "2.0"
    # Unsupported type falls back through NotImplemented, not an exception.
    assert (StrictVersion("1.0") == 123) is False
    assert (StrictVersion("1.0") != 123) is True


def test_strictversion_cmp_never_get_here_branch():
    class AlternatingBool:
        def __init__(self):
            self.calls = 0

        def __bool__(self):
            self.calls += 1
            return self.calls % 2 == 1

    left = object.__new__(StrictVersion)
    left.version = (1, 0, 0)
    flaky = AlternatingBool()
    left.prerelease = flaky

    right = StrictVersion("1.0")
    assert right.version == (1, 0, 0)
    assert right.prerelease is None

    with pytest.raises(AssertionError, match="never get here"):
        left._cmp(right)

    assert flaky.calls == 4
