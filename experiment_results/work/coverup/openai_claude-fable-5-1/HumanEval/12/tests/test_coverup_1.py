# file: script_12.py:4-20
# asked: {"lines": [14, 15, 17, 18, 19, 20], "branches": [[14, 15], [14, 17], [18, 0], [18, 19], [19, 18], [19, 20]]}
# gained: {"lines": [14, 15, 17, 18, 19, 20], "branches": [[14, 15], [14, 17], [18, 19], [19, 18], [19, 20]]}

from typing import List, Optional


def test_longest_empty_list() -> None:
    from script_12 import longest

    result: Optional[str] = longest([])
    assert result is None


def test_longest_single_element() -> None:
    from script_12 import longest

    result: Optional[str] = longest(["a"])
    assert result == "a"


def test_longest_unique_lengths() -> None:
    from script_12 import longest

    result: Optional[str] = longest(["a", "bb", "ccc"])
    assert result == "ccc"


def test_longest_tie_returns_first() -> None:
    from script_12 import longest

    result: Optional[str] = longest(["aa", "bb", "cc"])
    assert result == "aa"


def test_longest_first_is_longest() -> None:
    from script_12 import longest

    result: Optional[str] = longest(["aaaa", "bb", "ccc"])
    assert result == "aaaa"
