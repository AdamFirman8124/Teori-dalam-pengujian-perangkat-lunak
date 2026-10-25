# file: project/f035/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f035 import max_element


def test_max_element_updates_and_preserves_current_maximum():
    values = [3, 1, 5, 2]

    result = max_element(values)

    assert result == 5
