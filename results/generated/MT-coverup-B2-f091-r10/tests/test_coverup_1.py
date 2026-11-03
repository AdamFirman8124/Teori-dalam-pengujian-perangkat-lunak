# file: project/f091/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import re

from f091 import is_bored


def test_is_bored_counts_sentences_starting_with_i():
    # Sentences are split on '.', '?' or '!' plus optional whitespace.
    assert is_bored("I love it.") == 1
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("Hello world") == 0
    assert is_bored("I am bored! I want to sleep? I need coffee.") == 3
    assert is_bored("You and I. I and you.") == 1
    assert is_bored("Is it? I think so.") == 1


def test_is_bored_edge_cases():
    # Empty string splits into a single empty sentence, which does not count.
    assert is_bored("") == 0
    # A bare 'I' is not followed by a space, so it does not count.
    assert is_bored("I") == 0
    # 'I ' alone counts as a sentence starting with 'I '.
    assert is_bored("I ") == 1
    # Delimiters without trailing whitespace still split sentences.
    assert is_bored("I am here.I am there") == 2
    # Consecutive delimiters produce empty sentences that do not count.
    assert is_bored("I go!!I stop") == 2


def test_is_bored_uses_re_split(monkeypatch):
    # Verify the function delegates to re.split with the expected pattern;
    # monkeypatch automatically restores re.split afterwards.
    calls = []
    real_split = re.split

    def fake_split(pattern, string):
        calls.append((pattern, string))
        return real_split(pattern, string)

    monkeypatch.setattr(re, "split", fake_split)
    assert is_bored("I am here.") == 1
    assert calls == [(r"[.?!]\s*", "I am here.")]
