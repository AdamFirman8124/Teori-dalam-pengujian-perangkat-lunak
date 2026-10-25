# file: project/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_parse_numeric_components():
    """Lines 314, 315, 316, 317, 318, 322: numeric components are converted to int."""
    lv = LooseVersion()
    lv.parse("1.5.1")

    assert lv.vstring == "1.5.1"
    assert lv.version == [1, 5, 1]
    assert all(isinstance(c, int) for c in lv.version)


def test_loose_version_parse_mixed_components():
    """Lines 314-322 including the ValueError branch (line 319-320): alphabetic
    components stay as strings, numeric ones become ints, separators dropped."""
    lv = LooseVersion()
    lv.parse("2.2beta29")

    assert lv.vstring == "2.2beta29"
    assert lv.version == [2, 2, "beta", 29]
    assert isinstance(lv.version[0], int)
    assert isinstance(lv.version[2], str)
    assert isinstance(lv.version[3], int)


def test_loose_version_parse_via_constructor():
    """Lines 314-322 also execute through __init__ when a vstring is given."""
    lv = LooseVersion("3.10a")

    assert lv.vstring == "3.10a"
    assert lv.version == [3, 10, "a"]


def test_loose_version_parse_preserves_string_form():
    """__str__ round-trips the stored vstring, confirming parse stored it (line 314)."""
    lv = LooseVersion("1.13++")

    assert str(lv) == "1.13++"
