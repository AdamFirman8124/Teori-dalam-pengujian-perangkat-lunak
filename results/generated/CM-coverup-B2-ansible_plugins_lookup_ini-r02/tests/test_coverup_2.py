# file: project/ansible/plugins/lookup/ini.py:92-119
# asked: {"lines": [96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}
# gained: {"lines": [96, 97, 100, 101, 102, 105, 106, 107, 108, 111, 112, 113, 116, 119], "branches": [[102, 105], [102, 119], [105, 106], [105, 111], [106, 107], [106, 111], [107, 106], [107, 108], [111, 112], [111, 116]]}

import pytest
from collections import defaultdict
from ansible.plugins.lookup.ini import _parse_params


def test_parse_empty_term():
    paramvals = {"file": "def", "section": "def"}
    result = _parse_params("", paramvals)
    assert result == []


def test_parse_single_word_no_equals():
    paramvals = {"file": "x"}
    result = _parse_params("hello", paramvals)
    assert result == ["hello"]


def test_parse_multiword_append_to_same_key():
    paramvals = {"file": "x"}
    result = _parse_params("hello world", paramvals)
    assert result == ["hello world"]


def test_parse_valid_key_transition():
    paramvals = {"file": "def", "section": "def"}
    result = _parse_params("mykey file=myfile", paramvals)
    assert result == ["mykey", "file=myfile"]


def test_parse_equals_without_valid_key_match_appends():
    paramvals = {"file": "def"}
    result = _parse_params("hello foo=bar", paramvals)
    assert result == ["hello foo=bar"]


def test_parse_empty_paramvals_no_inner_iteration():
    paramvals = {}
    result = _parse_params("a=b", paramvals)
    assert result == ["a=b"]


def test_parse_multiple_distinct_keys():
    paramvals = {"file": "", "section": ""}
    result = _parse_params("val1 file=f1 section=s1", paramvals)
    assert result == ["val1", "file=f1", "section=s1"]


def test_parse_same_key_twice_appends():
    paramvals = {"file": "", "section": ""}
    result = _parse_params("file=a file=b", paramvals)
    assert result == ["file=a file=b"]


def test_parse_value_with_spaces():
    paramvals = {"file": "", "section": ""}
    result = _parse_params("file=my file with spaces", paramvals)
    assert result == ["file=my file with spaces"]


def test_parse_phrase_matching_multiple_valid_keys_last_wins():
    paramvals = {"file": "", "section": ""}
    result = _parse_params("file=section=val", paramvals)
    # both 'file=' and 'section=' are substrings, so thiskey ends as 'section'
    assert result == ["file=section=val"]
