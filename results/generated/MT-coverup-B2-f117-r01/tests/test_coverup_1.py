# file: project/f117/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [6, 7], [6, 9], [7, 6], [7, 8], [9, 4], [9, 10]]}

from f117 import select_words


def test_select_words_matches_and_non_matches():
    """Covers lines 3-11: matching words are appended (line 10), others skipped."""
    # "Mary" -> M,r,y = 3 consonants; "had" -> h,d = 2; "a" -> 0;
    # "little" -> l,t,t,l = 4; "lamb" -> l,m,b = 3
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("Mary had a little lamb", 2) == ["had"]
    assert select_words("Mary had a little lamb", 7) == []


def test_select_words_empty_string():
    """Empty input: the word loop (line 4) body never runs; result stays empty."""
    assert select_words("", 0) == []
    assert select_words("", 5) == []


def test_select_words_all_vowels():
    """Words made only of vowels take the false branch of the check on line 7,
    so line 8 (n_consonants += 1) is never reached for them."""
    assert select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    assert select_words("a e i o u", 1) == []


def test_select_words_case_insensitive():
    """Uppercase letters are lowercased before the vowel check (line 7)."""
    # "HELLO" -> H,L,L = 3 consonants; "WORLD" -> W,R,L,D = 4 consonants
    assert select_words("HELLO WORLD", 3) == ["HELLO"]
    assert select_words("HELLO WORLD", 4) == ["WORLD"]


def test_select_words_simple():
    """Sanity check on a plain sentence."""
    # "simple" -> s,m,p,l = 4; "little" -> l,t,t,l = 4; "sentence" -> 5
    assert select_words("simple little sentence", 4) == ["simple", "little"]
