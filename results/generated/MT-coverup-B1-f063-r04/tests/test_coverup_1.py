# file: project/f063/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

from f063 import fibfib


def test_fibfib_base_cases():
    assert fibfib(0) == 0
    assert fibfib(1) == 0
    assert fibfib(2) == 1


def test_fibfib_recursive_case():
    assert fibfib(3) == 1
    assert fibfib(4) == 2
    assert fibfib(5) == 4
