# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

from f080 import is_happy


def test_len_zero_returns_false():
    assert is_happy("") is False


def test_len_one_returns_false():
    assert is_happy("a") is False


def test_len_two_returns_false():
    assert is_happy("ab") is False


def test_happy_minimal_returns_true():
    assert is_happy("abc") is True


def test_happy_longer_returns_true():
    # covers loop iterating multiple times then falling through to return True
    assert is_happy("abcd") is True


def test_unhappy_first_two_equal():
    # covers s[i] == s[i+1] True -> return False
    assert is_happy("aab") is False


def test_unhappy_last_two_equal():
    # covers s[i] != s[i+1] but s[i+1] == s[i+2] True -> return False
    assert is_happy("abb") is False


def test_unhappy_first_and_third_equal():
    # covers first two comparisons False but s[i] == s[i+2] True -> return False
    assert is_happy("aba") is False


def test_unhappy_on_second_window():
    # covers first window passing (all comparisons False) then failing on later iteration
    # window 0: a,b,c distinct -> continue; window 1: b,c,b has s[i]==s[i+2] -> False
    assert is_happy("abcb") is False
