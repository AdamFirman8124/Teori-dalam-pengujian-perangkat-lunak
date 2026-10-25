# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

import pytest

from pysnooper.utils import truncate


@pytest.mark.parametrize(
    ("string", "max_length"),
    [
        ("unchanged", None),
        ("short", 5),
        ("short", 10),
    ],
)
def test_truncate_returns_unchanged_string(string, max_length):
    assert truncate(string, max_length) == string


def test_truncate_shortens_string_and_preserves_both_ends():
    result = truncate("abcdefghij", 8)

    assert result == "ab...hij"
    assert len(result) == 8
