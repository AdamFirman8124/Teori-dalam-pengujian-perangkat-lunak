# file: project/semantic_release/helpers.py:9-13
# asked: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}
# gained: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}

import pytest

from semantic_release.helpers import format_arg


@pytest.mark.parametrize(
    "raw_value, expected",
    [
        ("hello", "'hello'"),
        ("  padded  ", "'padded'"),
        ("", "''"),
    ],
)
def test_format_arg_with_string(raw_value, expected):
    """A str argument takes the True branch: it is stripped and single-quoted."""
    result = format_arg(raw_value)
    assert result == expected
    # Postcondition: result is the stripped value wrapped in single quotes
    assert result.startswith("'") and result.endswith("'")
    assert result[1:-1] == raw_value.strip()


@pytest.mark.parametrize(
    "raw_value, expected",
    [
        (42, "42"),
        (3.14, "3.14"),
        (None, "None"),
        ([1, "a"], "[1, 'a']"),
        (True, "True"),
    ],
)
def test_format_arg_with_non_string(raw_value, expected):
    """A non-str argument takes the else branch: it is converted via str()."""
    result = format_arg(raw_value)
    assert result == expected
    assert result == str(raw_value)
