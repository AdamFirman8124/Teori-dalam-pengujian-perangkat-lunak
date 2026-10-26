# file: project/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

from ansible.module_utils.compat.version import LooseVersion


def test_looseversion_pure_numeric():
    v = LooseVersion("1.5.1")
    assert v.vstring == "1.5.1"
    assert v.version == [1, 5, 1]
    assert str(v) == "1.5.1"


def test_looseversion_mixed_numeric_and_alpha():
    v = LooseVersion("1.5.2b2")
    assert v.vstring == "1.5.2b2"
    # 'b' cannot be converted to int, exercises except ValueError: pass
    # '1', '5', '2', '2' exercise successful int(obj) conversion
    assert v.version == [1, 5, 2, "b", 2]
    assert str(v) == "1.5.2b2"


def test_looseversion_alpha_component_and_dot_filtering():
    v = LooseVersion("3.2.pl0")
    assert v.vstring == "3.2.pl0"
    # exercises filtering of '.' and '' from component_re.split,
    # successful int conversion ('3', '2', '0') and ValueError path ('pl')
    assert v.version == [3, 2, "pl", 0]
    assert str(v) == "3.2.pl0"


def test_looseversion_parse_empty_and_dots_only():
    v = LooseVersion()
    v.parse("")
    assert v.vstring == ""
    assert v.version == []

    v.parse(".")
    assert v.vstring == "."
    assert v.version == []

    # direct parse call overwrites previous state
    v.parse("3.10a")
    assert v.vstring == "3.10a"
    assert v.version == [3, 10, "a"]
