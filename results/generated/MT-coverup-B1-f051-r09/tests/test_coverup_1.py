# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f051 import remove_vowels


def test_remove_vowels():
    assert remove_vowels("Hello World") == "Hll Wrld"
    assert remove_vowels("AEIOUaeiou") == ""
    assert remove_vowels("rhythm") == "rhythm"
