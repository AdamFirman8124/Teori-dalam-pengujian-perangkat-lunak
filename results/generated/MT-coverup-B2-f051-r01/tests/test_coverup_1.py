# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import f051


def test_remove_vowels_mixed_case_text():
    # Exercises both branches of the comprehension condition:
    # consonants pass the filter (True branch), vowels are dropped (False branch),
    # and uppercase vowels exercise the .lower() call.
    # Note: "AEIOU" between the two spaces is fully removed, leaving exactly
    # two consecutive spaces before the trailing "aeiou" is also removed.
    result = f051.remove_vowels("Hello, World! AEIOU aeiou")
    assert result == "Hll, Wrld!  "


def test_remove_vowels_only_vowels():
    # Every character takes the False branch of the condition.
    assert f051.remove_vowels("aeiouAEIOU") == ""


def test_remove_vowels_no_vowels():
    # Every character takes the True branch of the condition.
    assert f051.remove_vowels("rhythm xyz 123") == "rhythm xyz 123"


def test_remove_vowels_empty_string():
    # Edge case: line 3 still executes with an empty iterable.
    assert f051.remove_vowels("") == ""
