# file: project/semantic_release/helpers.py:9-13
# asked: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}
# gained: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}

import pytest

from semantic_release.helpers import format_arg


def test_format_arg_string_is_stripped_and_quoted():
    result = format_arg("  hello world  ")

    assert result == "'hello world'"
    assert result.startswith("'") and result.endswith("'")


def test_format_arg_empty_string_is_quoted():
    assert format_arg("") == "''"


def test_format_arg_non_string_uses_str():
    assert format_arg(42) == "42"
    assert format_arg(None) == "None"
    assert format_arg([1, 2]) == "[1, 2]"
    assert format_arg(3.5) == "3.5"


def test_format_arg_str_subclass_falls_back_to_str():
    class MyStr(str):
        pass

    value = MyStr("  padded  ")

    # type(value) == str is False for subclasses, so no stripping/quoting happens
    assert format_arg(value) == "  padded  "
    assert not format_arg(value).startswith("'")
