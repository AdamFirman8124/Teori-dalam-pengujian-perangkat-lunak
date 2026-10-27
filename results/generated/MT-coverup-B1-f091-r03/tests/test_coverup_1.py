# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f091 import is_bored


def test_is_bored_two_bored_sentences():
    assert is_bored("I am bored. I am still bored.") == 2
    assert is_bored("I love you. I hate you.") == 2


def test_is_bored_no_bored_sentences():
    assert is_bored("Hello world. You are nice.") == 0
    assert is_bored("Hello world. This is great! Are you bored?") == 0


def test_is_bored_mixed_punctuation():
    assert is_bored("I am bored? You are not! I am still bored.") == 2
    assert is_bored("I love it! You hate it? I like it.") == 2
    assert is_bored("I went home. You went home. I stayed.") == 2


def test_is_bored_edge_cases():
    assert is_bored("") == 0
    assert is_bored("I") == 0
    assert is_bored("I am here") == 1
    assert is_bored("I ") == 1
    assert is_bored("Ice cream is good.") == 0
    assert is_bored(" I am bored.") == 0
