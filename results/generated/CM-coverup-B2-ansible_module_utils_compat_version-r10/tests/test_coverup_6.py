# file: project/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_parse_numeric_components():
    lv = LooseVersion()
    lv.parse("1.5.1")
    assert lv.vstring == "1.5.1"
    assert lv.version == [1, 5, 1]


def test_loose_version_parse_mixed_components():
    # Exercises both the int() conversion (line 318) and the
    # ValueError -> pass branch (lines 319-320) for alpha parts.
    lv = LooseVersion()
    lv.parse("2.2beta29")
    assert lv.vstring == "2.2beta29"
    assert lv.version == [2, 2, "beta", 29]


def test_loose_version_parse_alpha_only():
    lv = LooseVersion()
    lv.parse("2g6")
    assert lv.vstring == "2g6"
    assert lv.version == [2, "g", 6]


def test_loose_version_init_parses_when_given_string():
    lv = LooseVersion("3.4j")
    assert lv.vstring == "3.4j"
    assert lv.version == [3, 4, "j"]


def test_loose_version_parse_drops_empty_and_dot_components():
    lv = LooseVersion()
    lv.parse("1.13++")
    assert lv.vstring == "1.13++"
    assert lv.version == [1, 13, "++"]
