# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

def test_is_bored_counts_sentences_starting_with_i():
    from f091 import is_bored

    assert is_bored("I am bored. Are you? I think so!") == 2
    assert is_bored("You are bored. Am I?") == 0
