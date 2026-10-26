# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

from f117 import select_words


def test_select_words_basic_n4():
    # Mary=3 (M,r,y), had=2, a=0, little=4, lamb=3
    assert select_words("Mary had a little lamb", 4) == ["little"]


def test_select_words_basic_n3():
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]


def test_select_words_empty_string():
    assert select_words("", 4) == []


def test_select_words_no_match():
    assert select_words("simple little time", 1) == []


def test_select_words_case_insensitive_vowels():
    # 'E' lowered is a vowel, so bEd has 2 consonants
    assert select_words("bEd", 2) == ["bEd"]


def test_select_words_multiple_matches_and_order():
    # uncle=3, our=1, who=2, used=2
    assert select_words("uncle our who used", 2) == ["who", "used"]


def test_select_words_zero_consonants():
    assert select_words("aeiou hello", 0) == ["aeiou"]


def test_select_words_whitespace_splitting():
    assert select_words("  cat\tdog  ", 2) == ["cat", "dog"]
