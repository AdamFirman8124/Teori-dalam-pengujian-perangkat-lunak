# file: project/ansible/plugins/lookup/ini.py:92-119
# asked: {"lines": [96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}
# gained: {"lines": [96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}

import pytest

from ansible.plugins.lookup.ini import _parse_params


def test_parse_params_first_term_and_key_update():
    """Covers lines 96-119: first-term branch (idp == 0) and key update via valid_keys."""
    term = "section=main key=value"
    paramvals = {"section": None, "key": None}
    result = _parse_params(term, paramvals)
    # 'section=main' becomes the value of 'section' (first term),
    # then 'key=value' switches thiskey to 'key' (line 108) and, being
    # empty, is stored as a new value (line 111-113).
    assert result == ["section=main", "key=value"]


def test_parse_params_append_to_existing_key():
    """Covers the else branch (line 116): appending to an existing key value."""
    term = "key=hello world"
    paramvals = {"key": None}
    result = _parse_params(term, paramvals)
    # 'key=hello' is the first term; 'world' has no '=' so it is appended
    # to the existing 'key' value with a space.
    assert result == ["key=hello world"]


def test_parse_params_lookup_item_default_key():
    """Covers the default thiskey='key' initialization for plain lookup items."""
    term = "foo bar"
    paramvals = {}
    result = _parse_params(term, paramvals)
    # No '=' anywhere, so thiskey stays 'key'; 'foo' is stored first,
    # 'bar' is appended to it.
    assert result == ["foo bar"]


def test_parse_params_empty_term():
    """Covers the loop-not-entered path: empty term yields an empty list."""
    assert _parse_params("", {"key": None}) == []


def test_parse_params_no_valid_key_match_keeps_current_key():
    """A phrase containing '=' that matches no valid key must not change thiskey."""
    term = "key=a unknown=b"
    paramvals = {"key": None}
    result = _parse_params(term, paramvals)
    # 'unknown=' is not in valid_keys, so thiskey remains 'key' and
    # 'unknown=b' is appended to the existing value.
    assert result == ["key=a unknown=b"]


def test_parse_params_does_not_mutate_paramvals():
    """Postcondition: the function must not modify the caller's paramvals dict."""
    paramvals = {"key": None, "section": None}
    original = dict(paramvals)
    _parse_params("section=main key=value", paramvals)
    assert paramvals == original
