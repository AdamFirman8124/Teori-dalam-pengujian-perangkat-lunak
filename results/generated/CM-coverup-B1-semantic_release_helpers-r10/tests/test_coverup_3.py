# file: project/semantic_release/helpers.py:9-13
# asked: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}
# gained: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}

from semantic_release.helpers import format_arg


def test_format_arg_str_strips_and_quotes():
    assert format_arg("  hello  ") == "'hello'"


def test_format_arg_str_empty():
    assert format_arg("") == "''"


def test_format_arg_non_str_int():
    assert format_arg(123) == "123"


def test_format_arg_non_str_none():
    assert format_arg(None) == "None"
