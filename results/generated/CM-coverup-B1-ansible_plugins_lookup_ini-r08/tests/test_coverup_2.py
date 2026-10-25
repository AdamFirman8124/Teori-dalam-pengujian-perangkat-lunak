# file: project/ansible/plugins/lookup/ini.py:92-119
# asked: {"lines": [96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}
# gained: {"lines": [96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}

from ansible.plugins.lookup.ini import _parse_params


def test_parse_params_empty_term_returns_empty_list():
    paramvals = {"key": "", "section": "global", "file": ""}

    result = _parse_params("", paramvals)

    assert result == []
    assert paramvals == {"key": "", "section": "global", "file": ""}


def test_parse_params_single_bare_key():
    paramvals = {"key": "", "section": "global", "file": ""}

    result = _parse_params("mykey", paramvals)

    assert result == ["mykey"]


def test_parse_params_bare_key_with_spaces_is_appended():
    paramvals = {"key": "", "section": "global", "file": ""}

    result = _parse_params("my key with spaces", paramvals)

    assert result == ["my key with spaces"]


def test_parse_params_key_value_pairs_in_order():
    paramvals = {"key": "", "section": "global", "file": "", "default": ""}

    result = _parse_params(
        "mykey section=global file=/path/to/file.ini", paramvals
    )

    assert result == ["mykey", "section=global", "file=/path/to/file.ini"]


def test_parse_params_first_phrase_is_key_value():
    paramvals = {"key": "", "section": "global", "file": ""}

    result = _parse_params("section=global mykey", paramvals)

    # After ``section=global``, ``thiskey`` remains ``section``, so the
    # following bare word is appended to the existing section value.
    assert result == ["section=global mykey"]


def test_parse_params_values_with_spaces_are_preserved():
    paramvals = {"key": "", "section": "global", "file": ""}

    result = _parse_params(
        "key=my key section=my section file=my file.ini", paramvals
    )

    assert result == [
        "key=my key",
        "section=my section",
        "file=my file.ini",
    ]


def test_parse_params_equals_without_valid_key_keeps_current_key():
    paramvals = {"key": "", "section": "global"}

    result = _parse_params("mykey foo=bar baz", paramvals)

    assert result == ["mykey foo=bar baz"]


def test_parse_params_empty_paramvals_uses_default_key():
    paramvals = {}

    result = _parse_params("a=b c", paramvals)

    assert result == ["a=b c"]
    assert paramvals == {}


def test_parse_params_repeated_key_appends_without_duplicate_entry():
    paramvals = {"key": "", "section": "global"}

    result = _parse_params("mykey section=one section=two", paramvals)

    assert result == ["mykey", "section=one section=two"]


def test_parse_params_multiple_valid_keys_in_one_phrase_last_match_wins():
    paramvals = {"key": "", "section": "global"}

    result = _parse_params("key=section=value", paramvals)

    assert result == ["key=section=value"]


def test_parse_params_valid_key_as_substring_sets_current_key():
    paramvals = {"key": "", "section": "global"}

    result = _parse_params("mykey xkey=value", paramvals)

    assert result == ["mykey xkey=value"]


def test_parse_params_new_key_after_bare_key_starts_new_entry():
    paramvals = {"key": "", "section": "global", "file": ""}

    result = _parse_params("lookup section=global file=test.ini", paramvals)

    assert result == ["lookup", "section=global", "file=test.ini"]
