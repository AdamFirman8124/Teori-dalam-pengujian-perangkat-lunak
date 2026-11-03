# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f086 import anti_shuffle


def test_single_word_characters_sorted():
    # Loop body executes; sorted(list(i)) reorders characters within a word.
    assert anti_shuffle('hello') == 'ehllo'


def test_word_already_sorted_unchanged():
    # Uppercase letters sort before lowercase ones (ASCII order).
    assert anti_shuffle('Hi') == 'Hi'


def test_multiple_words_sorted_independently():
    # Words are sorted independently and rejoined with single spaces.
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'


def test_digits_sorted():
    assert anti_shuffle('4321') == '1234'


def test_empty_string():
    # ''.split(' ') -> ['']; sorted(list('')) -> []; ''.join([]) -> ''.
    assert anti_shuffle('') == ''


def test_only_spaces():
    # Every token is the empty string; empty tokens are preserved.
    assert anti_shuffle('   ') == '   '


def test_consecutive_spaces_preserved():
    # Empty token between words exercises sorted(list('')) branch.
    assert anti_shuffle('ba  ab') == 'ab  ab'


def test_splitter_returning_no_tokens_branch():
    # Covers the comprehension branch where the loop body never runs
    # (s.split(' ') yields no tokens), which no str input can produce.
    class _EmptySplitter:
        def split(self, sep):
            assert sep == ' '
            return []

    assert anti_shuffle(_EmptySplitter()) == ''


def test_splitter_returning_multiple_tokens_branch():
    # Covers the comprehension branch with several iterations.
    class _MultiSplitter:
        def split(self, sep):
            assert sep == ' '
            return ['ba', 'dc', '']

    assert anti_shuffle(_MultiSplitter()) == 'ab cd '
