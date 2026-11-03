# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f086.anti_shuffle.

These tests ensure that line 3 (the return statement containing the
list-comprehension over s.split(' ')) is executed. The function is pure
(no I/O, no module-level or global state), so each test leaves no state
behind and no monkeypatching/teardown is required.
"""

from f086 import anti_shuffle


def test_anti_shuffle_single_word_sorts_characters():
    # Exercises line 3 with a single word whose characters need sorting.
    assert anti_shuffle('ba') == 'ab'


def test_anti_shuffle_multiple_words():
    # Exercises line 3 with multiple space-separated words.
    # 'Hello' is already sorted (ord('H') < ord('e') < ...),
    # 'World!!!' sorts to '!!!Wdlor'.
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'


def test_anti_shuffle_empty_string():
    # Exercises line 3 with an empty input; ''.split(' ') == [''] -> ''.
    assert anti_shuffle('') == ''


def test_anti_shuffle_preserves_word_boundaries():
    # Words are sorted independently; word order and separators are kept.
    assert anti_shuffle('ba dc') == 'ab cd'


def test_anti_shuffle_consecutive_spaces_produce_empty_words():
    # Consecutive spaces yield empty "words" that are preserved by the join.
    assert anti_shuffle('ba  dc') == 'ab  cd'


def test_anti_shuffle_numbers_and_mixed_case():
    # Sorting is by ordinal value: digits before uppercase before lowercase.
    assert anti_shuffle('b1A a') == '1Ab a'
