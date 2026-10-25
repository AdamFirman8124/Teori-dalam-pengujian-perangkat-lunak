# file: project/f055/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}

from f055 import fib


def test_fib_covers_base_cases_and_recursive_case():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(6) == 8
