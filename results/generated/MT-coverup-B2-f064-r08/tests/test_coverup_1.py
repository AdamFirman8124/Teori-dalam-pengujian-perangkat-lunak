# file: project/f064/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f064 import vowels_count


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("sky", 1),
        ("SKY", 1),
        ("cat", 1),
        ("AEIOU", 5),
    ],
)
def test_vowels_count_handles_vowels_and_final_y(value, expected):
    assert vowels_count(value) == expected


def test_vowels_count_does_not_count_non_final_y_as_a_vowel():
    value = "yellow"
    assert vowels_count(value) == 2
