# file: project/semantic_release/helpers.py:9-13
# asked: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}
# gained: {"lines": [10, 11, 13], "branches": [[10, 11], [10, 13]]}

import pytest

from semantic_release.helpers import format_arg


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("  hello  ", "'hello'"),
        ("hello", "'hello'"),
    ],
)
def test_format_arg_formats_strings(value, expected):
    assert format_arg(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (123, "123"),
        (None, "None"),
        (True, "True"),
    ],
)
def test_format_arg_formats_non_strings(value, expected):
    assert format_arg(value) == expected
