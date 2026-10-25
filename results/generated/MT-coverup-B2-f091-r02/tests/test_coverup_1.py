# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import f091


def test_is_bored_counts_sentences_starting_with_I():
    text = "I am bored. I like it! You are here? I am done."
    assert f091.is_bored(text) == 3


def test_is_bored_returns_zero_when_no_sentence_starts_with_I():
    assert f091.is_bored("Hello there. You are fine!") == 0


def test_is_bored_handles_empty_string():
    assert f091.is_bored("") == 0


def test_is_bored_handles_single_sentence_without_terminator():
    assert f091.is_bored("I am bored") == 1
    assert f091.is_bored("Bored I am") == 0


def test_is_bored_ignores_lowercase_i_and_bare_I():
    assert f091.is_bored("i am bored. So I am. I") == 0


def test_is_bored_handles_trailing_and_repeated_separators():
    assert f091.is_bored("I am bored.") == 1
    assert f091.is_bored("I am bored...  I am tired?!") == 2
    assert f091.is_bored("...") == 0


def test_is_bored_does_not_mutate_input_or_module_state(monkeypatch):
    text = "I am bored. You are fine."
    original = str(text)
    before = dict(vars(f091))
    assert f091.is_bored(text) == 1
    assert text == original
    assert dict(vars(f091)) == before
