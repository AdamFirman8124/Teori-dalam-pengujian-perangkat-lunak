# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f007 import filter_by_substring


def test_filter_by_substring_with_matches():
    """Covers line 6 with both the True branch of 'substring in x'."""
    result = filter_by_substring(["abc", "bcd", "cde", "array"], "a")
    assert result == ["abc", "array"]


def test_filter_by_substring_no_matches():
    """Covers the False branch of 'substring in x'."""
    result = filter_by_substring(["abc", "bcd", "cde"], "xyz")
    assert result == []


def test_filter_by_substring_empty_input_list():
    """Covers iterating over an empty list (comprehension yields empty list)."""
    result = filter_by_substring([], "a")
    assert result == []


def test_filter_by_substring_empty_substring_matches_all():
    """Empty substring is contained in every string (True branch for all items)."""
    result = filter_by_substring(["abc", "def"], "")
    assert result == ["abc", "def"]


def test_filter_by_substring_mixed_branches_and_original_untouched():
    """Covers both branches in a single call and verifies input is not mutated."""
    strings = ["hello", "world", "help"]
    result = filter_by_substring(strings, "hel")
    assert result == ["hello", "help"]
    assert strings == ["hello", "world", "help"]
