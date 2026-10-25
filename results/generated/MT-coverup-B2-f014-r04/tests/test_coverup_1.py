# file: project/f014/__init__.py:4-10
# asked: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}
# gained: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}

from f014 import all_prefixes


def test_all_prefixes_empty_string():
    result = all_prefixes("")
    assert result == []
    assert isinstance(result, list)
    assert len(result) == 0


def test_all_prefixes_single_character():
    result = all_prefixes("a")
    assert result == ["a"]
    assert len(result) == 1


def test_all_prefixes_multiple_characters():
    result = all_prefixes("abc")
    assert result == ["a", "ab", "abc"]
    assert len(result) == 3
    assert result[0] == "a"
    assert result[-1] == "abc"
    for i, prefix in enumerate(result):
        assert prefix == "abc"[: i + 1]
        assert len(prefix) == i + 1


def test_all_prefixes_longer_string():
    result = all_prefixes("hello")
    assert result == ["h", "he", "hel", "hell", "hello"]
    assert len(result) == len("hello")
