# file: project/semantic_release/helpers.py:9-13
# asked: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}
# gained: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}

from semantic_release.helpers import format_arg


def test_format_arg_strips_and_quotes_string():
    assert format_arg("  value  ") == "'value'"


def test_format_arg_converts_non_string_to_string():
    assert format_arg(42) == "42"
