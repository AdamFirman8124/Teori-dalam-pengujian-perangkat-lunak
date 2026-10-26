# file: project/semantic_release/helpers.py:9-13
# asked: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}
# gained: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}

from semantic_release.helpers import format_arg


def test_format_arg_strips_whitespace_and_quotes_strings():
    assert format_arg("  release  ") == "'release'"


def test_format_arg_converts_non_strings_to_strings():
    assert format_arg(42) == "42"
