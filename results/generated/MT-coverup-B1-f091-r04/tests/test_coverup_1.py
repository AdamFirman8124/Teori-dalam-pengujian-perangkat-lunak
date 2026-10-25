# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f091 import is_bored


def test_is_bored_counts_sentences_starting_with_i():
    text = "I am bored. You are not! I feel tired? I'm fine."
    assert is_bored(text) == 2
