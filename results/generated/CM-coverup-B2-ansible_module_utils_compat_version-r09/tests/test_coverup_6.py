# file: project/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


@pytest.mark.parametrize(
    "vstring,expected",
    [
        # Purely numeric components: exercise the successful int() conversion
        # branch (lines 317-318).
        ("1.5.1", [1, 5, 1]),
        ("161", [161]),
        ("8.02", [8, 2]),
        # Mixed numeric/alphabetic: exercise both the int() success branch and
        # the ValueError handling branch (lines 319-320).
        ("1.5.2b2", [1, 5, 2, "b", 2]),
        ("2.2beta29", [2, 2, "beta", 29]),
        ("3.2.pl0", [3, 2, "pl", 0]),
        # Purely alphabetic: every component takes the ValueError branch.
        ("abc", ["abc"]),
        ("5.5.kw", [5, 5, "kw"]),
        # Characters not matched by component_re remain grouped as one string,
        # which also lands in the ValueError branch.
        ("1.13++", [1, 13, "++"]),
        # Only separators: the list-comprehension filter (line 315) drops every
        # '.' and the surrounding empty strings, yielding an empty version.
        ("..", []),
        # Empty string: the single empty split result is removed by the filter.
        ("", []),
    ],
)
def test_loose_version_parse_covers_all_branches(vstring, expected):
    version = LooseVersion()
    version.parse(vstring)

    # Line 314: vstring must be stored verbatim (it backs __str__).
    assert version.vstring == vstring
    # Line 322: the parsed component list must be stored on .version.
    assert version.version == expected
    # Numeric parts were converted to int, everything else stayed a string.
    assert all(isinstance(c, int) or isinstance(c, str) for c in version.version)


def test_loose_version_init_delegates_to_parse():
    version = LooseVersion("3.4j")
    assert version.vstring == "3.4j"
    assert version.version == [3, 4, "j"]


def test_parse_does_not_share_state_between_instances():
    first = LooseVersion("1.2")
    second = LooseVersion("9.8.7")
    assert first.version == [1, 2]
    assert second.version == [9, 8, 7]
    assert first.vstring == "1.2"
    assert second.vstring == "9.8.7"
