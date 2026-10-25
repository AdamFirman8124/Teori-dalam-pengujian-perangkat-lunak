# file: project/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_parse_mixed_components():
    """Exercise all lines 314-322 of LooseVersion.parse.

    A mixed version string forces:
      - line 314: vstring stored
      - line 315: component_re.split() filtering out empty strings and '.'
      - line 316: loop over components
      - line 318: int() conversion of numeric components
      - line 319-320: ValueError pass for alphabetic components
      - line 322: self.version assignment
    """
    lv = LooseVersion()
    lv.parse("1.5.2b2")

    assert lv.vstring == "1.5.2b2"
    assert lv.version == [1, 5, 2, "b", 2]


def test_loose_version_parse_all_alpha():
    """Cover the ValueError branch (lines 319-320) with no numeric parts."""
    lv = LooseVersion()
    lv.parse("abc")

    assert lv.vstring == "abc"
    assert lv.version == ["abc"]


def test_loose_version_parse_via_constructor():
    """Cover parse() through __init__ as well."""
    lv = LooseVersion("3.4j")
    assert lv.version == [3, 4, "j"]
    assert str(lv) == "3.4j"
