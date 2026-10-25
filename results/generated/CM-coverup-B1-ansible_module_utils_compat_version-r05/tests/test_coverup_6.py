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
    # ValueError -> pass branch (lines 319-320), plus '.' filtering.
    lv = LooseVersion()
    lv.parse("2.2beta29")
    assert lv.vstring == "2.2beta29"
    assert lv.version == [2, 2, "beta", 29]


def test_loose_version_parse_alpha_only():
    lv = LooseVersion()
    lv.parse("11g")
    assert lv.vstring == "11g"
    assert lv.version == [11, "g"]


def test_loose_version_parse_via_constructor():
    lv = LooseVersion("3.10a")
    assert lv.vstring == "3.10a"
    assert lv.version == [3, 10, "a"]


def test_loose_version_parse_preserves_leading_zeros_as_ints():
    lv = LooseVersion()
    lv.parse("8.02")
    assert lv.version == [8, 2]
    assert str(lv) == "8.02"
