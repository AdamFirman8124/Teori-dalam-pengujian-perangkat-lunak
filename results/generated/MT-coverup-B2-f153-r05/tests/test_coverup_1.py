# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

from f153 import Strongest_Extension


def test_strongest_extension_selects_highest_score_and_keeps_first_on_tie():
    extensions = ["lower", "AbC", "XYZ", "ABC"]

    result = Strongest_Extension("Example", extensions)

    assert result == "Example.XYZ"
    assert extensions == ["lower", "AbC", "XYZ", "ABC"]
