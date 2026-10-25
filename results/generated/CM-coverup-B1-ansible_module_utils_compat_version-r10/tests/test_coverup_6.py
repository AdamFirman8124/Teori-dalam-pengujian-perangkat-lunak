# file: project/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

from ansible.module_utils.compat.version import LooseVersion


def test_looseversion_parse_numeric_only():
    lv = LooseVersion("1.5.1")
    assert lv.vstring == "1.5.1"
    assert lv.version == [1, 5, 1]
    assert str(lv) == "1.5.1"


def test_looseversion_parse_mixed_alpha_numeric():
    lv = LooseVersion("1.5.2b2")
    assert lv.vstring == "1.5.2b2"
    # 'b' cannot be converted to int, exercises except ValueError: pass
    assert lv.version == [1, 5, 2, "b", 2]


def test_looseversion_parse_word_component():
    lv = LooseVersion("3.2.pl0")
    assert lv.vstring == "3.2.pl0"
    assert lv.version == [3, 2, "pl", 0]


def test_looseversion_parse_filters_dots_and_empties():
    lv = LooseVersion()
    lv.parse("1.5.1")
    assert lv.vstring == "1.5.1"
    assert lv.version == [1, 5, 1]
    assert "." not in lv.version
    assert "" not in lv.version


def test_looseversion_parse_empty_component_list():
    # "." splits to ['', '.', ''] which is fully filtered, so the
    # for loop body (try int()/except) executes zero times
    lv = LooseVersion()
    lv.parse(".")
    assert lv.vstring == "."
    assert lv.version == []
