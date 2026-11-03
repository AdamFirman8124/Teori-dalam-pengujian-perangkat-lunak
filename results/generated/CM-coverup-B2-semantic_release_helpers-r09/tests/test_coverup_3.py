# file: project/semantic_release/helpers.py:9-13
# asked: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}
# gained: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}

import pytest

from semantic_release.helpers import format_arg


def test_format_arg_with_string():
    """Lines 10-11: a str value is stripped and wrapped in single quotes."""
    result = format_arg("  hello world  ")
    assert result == "'hello world'"
    # The surrounding single quotes must be present
    assert result.startswith("'") and result.endswith("'")
    # Leading/trailing whitespace must have been stripped
    assert not result.strip("'").startswith(" ")
    assert not result.strip("'").endswith(" ")


def test_format_arg_with_plain_string():
    """A string without surrounding whitespace still gets quoted."""
    assert format_arg("abc") == "'abc'"


def test_format_arg_with_non_string_int():
    """Line 13: a non-str value is converted with str()."""
    assert format_arg(42) == "42"


def test_format_arg_with_non_string_list():
    """Line 13: non-str containers are stringified via str()."""
    assert format_arg([1, "a"]) == "[1, 'a']"


def test_format_arg_with_none():
    """Line 13: None is stringified via str()."""
    assert format_arg(None) == "None"
