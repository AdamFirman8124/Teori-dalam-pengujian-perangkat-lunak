# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f029 import filter_by_prefix


def test_filter_by_prefix_includes_matches_and_excludes_nonmatches():
    strings = ["prefix_one", "other", "prefix_two"]
    original = strings.copy()

    result = filter_by_prefix(strings, "prefix")

    assert result == ["prefix_one", "prefix_two"]
    assert strings == original
