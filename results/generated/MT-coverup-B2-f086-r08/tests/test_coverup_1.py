# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f086 import anti_shuffle


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", ""),
        ("hello", "ehllo"),
        ("Hello World", "Hello Wdlor"),
        ("a", "a"),
        ("cba fed", "abc def"),
        ("  ", "  "),
        ("a  b", "a  b"),
        (" leading", " adegiln"),
        ("trailing ", "agiilnrt "),
        ("Hello, World!", ",Hello !Wdlor"),
    ],
)
def test_anti_shuffle_sorts_each_word(s, expected):
    assert anti_shuffle(s) == expected


def test_anti_shuffle_preserves_word_count_and_spaces():
    s = "the quick  brown fox "
    result = anti_shuffle(s)

    assert result.count(" ") == s.count(" ")
    assert len(result.split(" ")) == len(s.split(" "))
    assert result.split(" ") == ["" if w == "" else "".join(sorted(w)) for w in s.split(" ")]


def test_anti_shuffle_output_words_are_permutations_of_input_words():
    s = "banana apple cherry"
    result = anti_shuffle(s)

    for original, shuffled in zip(s.split(" "), result.split(" ")):
        assert sorted(shuffled) == sorted(original)
        assert shuffled == "".join(sorted(original))


def test_anti_shuffle_does_not_mutate_input():
    s = "zebra yak"
    snapshot = str(s)

    anti_shuffle(s)

    assert s == snapshot
