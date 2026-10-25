# file: project/ansible/plugins/lookup/ini.py:92-119
# asked: {"lines": [96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}
# gained: {"lines": [96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}

from ansible.plugins.lookup.ini import _parse_params


def test_empty_term_returns_empty_list():
    assert _parse_params("", {"section": "global", "file": "ansible.ini"}) == []
    assert _parse_params("   ", {}) == []


def test_single_term_defaults_to_key():
    assert _parse_params("mykey", {"section": "global", "file": "ansible.ini"}) == ["mykey"]


def test_multiword_appends_to_same_key():
    # no '=' in phrases, second phrase takes else branch
    assert _parse_params("hello world", {}) == ["hello world"]


def test_equals_with_empty_valid_keys():
    # '=' in phrase but valid_keys empty, so inner for loop has zero iterations
    assert _parse_params("a=b c=d", {}) == ["a=b c=d"]


def test_equals_without_matching_valid_key_appends():
    # '=' in phrase but ('section=' in phrase) is False, thiskey unchanged, else branch
    assert _parse_params("foo bar=baz", {"section": "global"}) == ["foo bar=baz"]


def test_switch_to_new_valid_key():
    # first phrase idp==0 branch, second phrase switches key and takes
    # idp!=0 and not params[thiskey] branch
    assert _parse_params("mykey section=production", {"section": "", "file": ""}) == [
        "mykey",
        "section=production",
    ]


def test_switch_to_second_valid_key():
    # covers inner if False for first k then True for second k in same loop
    assert _parse_params("mykey file=my.ini", {"section": "", "file": ""}) == [
        "mykey",
        "file=my.ini",
    ]


def test_append_with_space_to_switched_key():
    # third phrase has no '=', appends to switched key via else branch
    assert _parse_params("mykey section=foo bar", {"section": "", "file": ""}) == [
        "mykey",
        "section=foo bar",
    ]


def test_repeated_same_key_appends():
    # second phrase matches existing key with truthy value, takes else branch
    assert _parse_params("section=one section=two", {"section": "", "file": ""}) == [
        "section=one section=two"
    ]
