# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

from f112 import reverse_delete


def test_reverse_delete_filters_and_palindrome_check():
    # 'abcde' with 'b' removed -> 'acde', not a palindrome
    result = reverse_delete("abcde", "b")
    assert result == ("acde", False)

    # 'abcdedcba' with 'x' removed -> unchanged, palindrome
    result = reverse_delete("abcdedcba", "x")
    assert result == ("abcdedcba", True)

    # all chars removed -> empty string, palindrome
    result = reverse_delete("abc", "abc")
    assert result == ("", True)
