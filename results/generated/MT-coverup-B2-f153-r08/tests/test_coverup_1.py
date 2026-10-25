# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

from f153 import Strongest_Extension


def test_strongest_extension_selects_first_highest_scoring_extension():
    extensions = ["lower", "UPPER!", "OTHER?"]

    result = Strongest_Extension("Example", extensions)

    assert result == "Example.UPPER!"
    assert extensions == ["lower", "UPPER!", "OTHER?"]
