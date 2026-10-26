# file: project/semantic_release/helpers.py:9-13
# asked: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}
# gained: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}

from semantic_release.helpers import format_arg


def test_format_arg_str_with_whitespace():
    assert format_arg("  hello  ") == "'hello'"


def test_format_arg_str_without_whitespace():
    assert format_arg("hello") == "'hello'"


def test_format_arg_empty_string():
    assert format_arg("") == "''"


def test_format_arg_int():
    assert format_arg(42) == "42"


def test_format_arg_none():
    assert format_arg(None) == "None"
